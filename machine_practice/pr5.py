# PythonML Practice5: 다중 분류
# 데이터셋: seaborn diamonds dataset (다이아몬드 세공 품질 'cut' 다중 분류)
#
import seaborn as sns
# [단계 1] 데이터 로드 및 전처리, 독립/종속 변수 분리
# 1. seaborn의 'diamonds' 데이터셋을 로드하세요. (sns.load_dataset('diamonds'))
df = sns.load_dataset('diamonds')
# df.info()

#  #   Column   Non-Null Count  Dtype   
# ---  ------   --------------  -----   
#  0   carat    53940 non-null  float64 
#  1   cut      53940 non-null  category
#  2   color    53940 non-null  category
#  3   clarity  53940 non-null  category
#  4   depth    53940 non-null  float64 
#  5   table    53940 non-null  float64 
#  6   price    53940 non-null  int64   
#  7   x        53940 non-null  float64 
#  8   y        53940 non-null  float64 
#  9   z        53940 non-null  float64 
# dtypes: category(3), float64(6), int64(1)



# 2. 실습 연산 효율성을 위해 5,000개 샘플을 무작위 추출하세요. (df = df.sample(n=5000, random_state=42).reset_index(drop=True))
df = df.sample(n=5000, random_state=42).reset_index(drop=True)

# 3. 다이아몬드 커팅 품질('cut': Fair, Good, Very Good, Premium, Ideal)을 종속 변수 Y로, 나머지 컬럼을 독립 변수 X로 분리하세요.
#

X = df.drop['cut']
Y = df['cut']

# [단계 2] 훈련용 / 테스트용 데이터 분리
# train_test_split을 사용하여 8:2 비율(test_size=0.2)로 분리하고, 5개 클래스 비율 유지를 위해 stratify=Y, 재현성을 위해 random_state=42로 설정하세요.
#
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train , Y_test = train_test_split(X,Y,test_size=0.2,random_state=42, stratify= Y)

# [단계 3] ColumnTransformer를 활용한 복합 전처리 구성
# 1. 수치형 피처: ['carat', 'depth', 'table', 'price', 'x', 'y', 'z'] -> StandardScaler를 적용하세요.
# 2. 범주형 피처: ['color', 'clarity'] -> OneHotEncoder(drop='first', sparse_output=False )를 적용하세요.
# 3. 위 두 변환기를 ColumnTransformer로 묶어 'preprocessor' 객체를 정의하세요.
#
num_features = ['carat', 'depth', 'table', 'price', 'x', 'y', 'z']
cat_features= ['color', 'clarity']

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), num_features), 
    ('cat', OneHotEncoder(drop='first', sparse_output=False), cat_features )
    ])

# [단계 4] 파이프라인(Pipeline) 구축 및 기본 모델 학습
# 1. Pipeline을 생성하여 [단계 3]의 'preprocessor'와 LogisticRegression(max_iter=1000, random_state=42)을 단일 워크플로우로 연결하세요.
# 2. X_train 원본(DataFrame)과 Y_train을 파이프라인에 직접 투입하여 모델을 학습(fit)시키세요.
#
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

pipe = Pipeline([
    ('preprocessor', preprocessor),
    ('model',LogisticRegression(max_iter=1000, random_state=42)
)])

pipe.fit(X_train, Y_train)

# [단계 5] 모델 다중 분류 지표 산출 및 혼동 행렬 시각화
# 1. 테스트 세트(X_test)에 대한 예측 레이블(Y_pred) 및 예측 확률(Y_pred_proba)을 생성하세요.
Y_pred = pipe.predict(X_test)
Y_pred_proba = pipe.predict_proba(Y_pred)
print('정답지', pipe.classes_)

from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score    
# 2. 파이프라인 내부 분류기의 클래스 순서(classes_)를 확인하고, 다중 분류 4대 평가 지표를 산출하세요:
# 1) 정확도 : 전체 예측 건수 중 맞힌 정답의 비율  
# 클래스내 개수들이 불균형 이면 점수가 왜곡 발생 
print( accuracy_score( Y_test , Y_pred ) ) # 0.8125
# 2) 정밀도 : 예측 한 것 중 실제 로 맞힌 비율 
print( precision_score( Y_test , Y_pred , average="macro" ) )
# 3) 재현율 : 실제 정답인 것 중에 모델이 놓치지 않고 찾아낸 비율 
print( recall_score( Y_test , Y_pred  , average="macro") )
# 4) f1점수/표준 : 정밀도 와 재현율 간의 조화 조정하기 위한 조화평균 
print( f1_score( Y_test , Y_pred , average="macro" ))

#    - 정확도 (accuracy_score) 정밀도 (precision_score, average='macro') 재현율 (recall_score, average='macro') F1 점수 (f1_score, average='macro')
# 3. ConfusionMatrixDisplay.from_predictions를 활용해 혼동 행렬을 시각화하세요.
#
import matplotlib.pyplot as plt 
from sklearn.metrics import ConfusionMatrixDisplay , classification_report  
# ConfusionMatrixDisplay.from_predictions( 정답지 , 예측값 )
ConfusionMatrixDisplay.from_predictions( Y_test , Y_pred )
plt.show() 

print( classification_report( Y_test , Y_pred ) )


# [단계 6] GridSearchCV 기반 하이퍼파라미터 튜닝
from sklearn.model_selection import GridSearchCV

# 1. 규제 강도 탐색 그리드를 정의하세요: {'model__C': [0.01, 0.1, 1.0, 10.0]}
param_grid = {'model__C': [0.01, 0.1, 1.0, 10.0]}

# 2. StratifiedKFold(n_splits=5, shuffle=True, random_state=42) 교차 검증 객체를 생성하세요.
from sklearn.model_selection import StratifiedKFold
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)



# 3. scoring='f1_macro'를 기준으로 GridSearchCV를 수행하여 최적 파라미터와 최고 점수를 출력하세요.
grid = GridSearchCV(pipe, param_grid, cv=cv, scoring="f1_macro", n_jobs=-1)

# 4. 최적 추정기(best_estimator_)로 X_test를 평가하고 classification_report를 출력하세요.
#
best_model = grid.best_estimator_ 
Y_pred = best_model.predict(X_test) # 최적의 추정기로 예측

print(classification_report(Y_test,Y_pred)) # 파이프라인으로 최적의


# [단계 7] 파이프라인 직렬화(저장/불러오기) 및 신규 원본 데이터 실시간 추론
import joblib

# 1. joblib.dump를 사용하여 최적화된 파이프라인 전체를 './diamond_pipeline.pkl'로 저장하세요.
joblib.dump(pipe,'./diamond_pipeline.pkl')

# 2. joblib.load로 저장된 파이프라인을 다시 불러오세요.
pipe_load= joblib.load('./day14/fish_model.pkl')

# 3. 스케일링/인코딩을 거치지 않은 원본 형태의 임의 다이아몬드 샘플(DataFrame)을 생성하세요: (예: carat=0.7, color='E', clarity='SI1', depth=61.5, table=55.0, price=3000, x=5.7, y=5.75, z=3.5)
import pandas as pd
sample = pd.DataFrame(carat=0.7, color='E', clarity='SI1', depth=61.5, table=55.0, price=3000, x=5.7, y=5.75, z=3.5)


# 4. 불러온 파이프라인의 predict() 및 predict_proba()에 직접 전달하여 예측 커팅 등급(cut)과 가장 높은 확신도(최대 확률 %)를 출력하세요.

predict = pipe_load.predict( sample )
print('예측값:', predict)

