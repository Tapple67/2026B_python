## lightGBM 튜닝 / 서빙 예제 필요한 데이터셋
import pandas as pd

import pandas as pd
url = 'https://raw.githubusercontent.com/rashida048/Datasets/master/USA_cars_datasets.csv'
df = pd.read_csv(url)
#*만약에 모델의 성능 향상 하기 위한 도메인 지식의 특성 추가 좋다.*
df = df[df['price'] > 0]
num_cols = ['year', 'mileage']                                      #수치형
cat_cols = ['brand', 'model', 'title_status', 'color', 'state']     #범주형
# 범주형 자료들을 원핫 인코딩이 아닌 판다스,'카테고리' 타입 변경 # lightGBM 내장 원핫 인코딩 사용 목적

for col in cat_cols: 
    df[col] = df[col].astype('category')

X = df[num_cols + cat_cols]
Y = df['price']
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#1) 튜닝->optuna
# 1. optuna 설치: $env:PYYAML_FORCE_LIBYAML = "0", pip install optuna shap
#2)optuna 로그 숨기기/경고만 출력
import optuna
import numpy as np
optuna.logging.set_verbosity( optuna.logging.WARNING )
from lightgbm import LGBMRegressor, early_stopping
#4)목적함수 만들기, 콜백 함수(trial)
def objective(trial):
    #4-1 교차검증 KFold
    from sklearn.model_selection import KFold
    cv = KFold(n_splits=5, shuffle=True, random_state=42)
    cv_r2_scores = []
    best_iterations = []
    for train_idx, val_idx in cv.split(X_train,Y_train) :
        #훈련데이터 세트 내부에서 훈련용/검증용 분할 수행,k=5, 5개 폴드, 각각 한번씩 검증용
        X_tr,X_val = X_train.iloc[train_idx], X_train.iloc[val_idx]
        Y_tr,Y_val = Y_train.iloc[train_idx], Y_train.iloc[val_idx]
        # k폴드에서 분할한 훈련용 모델 만들기
        model = LGBMRegressor(
            n_estimators=1000,
            # trial.suggest_XXX('파라미터명', 시작값, 끝값)
            learning_rate=trial.suggest_float('learning_rate', 0.01, 0.1), # 학습률
            num_leaves=trial.suggest_int('num_leaves',10,30),
            max_depth=trial.suggest_int( 'max_depth' , 3 , 10 ),
            min_child_samples=trial.suggest_int('min_child_samples', 10, 50),
            subsample=trial.suggest_float('subsample', 0.6, 1.0),
            subsample_freq=1, verbose=-1,random_state=42, n_jobs=-1,
            colsample_bytree=trial.suggest_float('colsample_bytree', 0.6, 1.0 )
            #class_weight 회귀 모델 이므로 생략
        )
        #폴드별 훈련용/검증용 으로 학습
        model.fit(X_tr, Y_tr,
                  eval_set=[(X_val, Y_val)],
                  callbacks=[early_stopping(stopping_rounds=50, verbose=False)] )
        #kFold별 검증 쳥가 r2
        r2 = model.score(X_val, Y_val)
        cv_r2_scores.append(r2)
        best_iterations.append(model.best_iteration_)

    #k 폴드에서 산출된 최적 트리 개수의 평균값을 trial의 속성으로 저장
    trial.set_user_attr('best_n_estimators', int(np.mean(best_iterations)))
    return np.mean(cv_r2_scores)

#3)  optuna.create_study(direction='maximize'/'minimize')
#현재 실습은 회귀 모델아며 r2 결정계수 평가 지표 사용할 예정
sampler = optuna.samplers.TPESampler(seed=42)
study = optuna.create_study(direction='maximize', sampler=sampler )
# study.optimize(목적함수, n_trials=반복수) -> 반복수 만큼 목적함수 실행
study.optimize(objective, n_trials=20)

#5) 최적 모델
print('최적하이퍼파라미터:', study.best_params)
optimal_model = study.best_trial.user_attrs['best_n_estimators']
print( '최적 트리: ', optimal_model )

#6) 최적 파라미터로 모델 학습
final_model = LGBMRegressor(
    random_state=42,verbose =-1, n_jobs=-1,
    **study.best_params,
    n_estimators=optimal_model
)
final_model.fit(X_train,Y_train)
print("- Train r2:", final_model.score(X_train, Y_train))
print("- Test r2 :", final_model.score(X_test, Y_test))
print("특성 이름   :", final_model.feature_names_in_)
print("특성 중요도  :", final_model.feature_importances_)

# - Train r2: 0.8019492459052838
# - Test r2 : 0.7205797276257827
# 특성 이름   : ['year' 'mileage' 'brand' 'model' 'title_status' 'color' 'state']
# 특성 중요도  : [310 870 200 389  50 228 467]

#7) joblib 저장/로드
import joblib
# joblib.dump(final_model, './day18/gbm_model.pkl') # 1)

loaded_model = joblib.load("./day18/gbm_model.pkl")

new_cars = pd.DataFrame([
  {'year': 2019, 'mileage': 25000, 'brand': 'ford', 'model': 'f-150', 'title_status': 'clean vehicle',  'color': 'white', 'state': 'texas'},
  {'year': 2014, 'mileage': 85000, 'brand': 'nissan', 'model': 'altima', 'title_status': 'salvage insurance', 'color': 'black', 'state': 'california'}
])

for col in cat_cols:
    new_cars[col] = new_cars[col].astype(X_train[col].dtype)

serving_preds = loaded_model.predict(new_cars)
print("서빙 모델 예측 가격 (1번 차량) :", serving_preds[0])
print("서빙 모델 예측 가격 (2번 차량) :", serving_preds[1])

# 서빙 모델 예측 가격 (1번 차량) : 27983.4777071311
# 서빙 모델 예측 가격 (2번 차량) : 635.4763331040908