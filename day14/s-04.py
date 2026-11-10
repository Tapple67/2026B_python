import pandas as pd
df = pd.read_csv("./Fish.csv")
X = df[['Length2','Height', 'Width']] # 특정 선정/구성
Y = df['Weight'] #타깃

#3) 훈련/테스트 분리
from sklearn.model_selection import GridSearchCV, KFold, train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#4) 과소 적합 방지 하고자 항 추가 PolynomialFeatures # 제곱/곱셈
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2, include_bias=False) #degree=2 기본값
poly.fit(X_train)
X_train_poly = poly.transform(X_train)
X_test_poly = poly.transform(X_test)

# 5) 항 많아지면 항/특성 간에 단위 표준화 / 스케일링
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(X_train_poly)
X_train_scaled = ss.transform(X_train_poly)
X_test_scaled = ss.transform(X_test_poly)

#6) 모델 선택 = 단순 선형회귀, 규제(릿지/라쏘) alpha 규제 강도
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train_scaled,Y_train)

#7) 결정계수
print('r2: ', model.score(X_train_scaled,Y_train))
print('r2: ', model.score(X_test_scaled,Y_test))

# r2:  0.9833194466740022
# r2:  0.971937241576259

#=================================== (4)~(6) 묶음
from sklearn.pipeline import Pipeline
pipe_model = Pipeline([
    ('poly', PolynomialFeatures(degree=2,include_bias=False)), # 4
    ('scaler', StandardScaler() ),  #5
    ('regressor', LinearRegression() ) #6
])
#9) 파이프라인 으로 학습
pipe_model.fit(X_train, Y_train)
print('r2: ', model.score(X_train_scaled,Y_train))
print('r2: ', model.score(X_test_scaled,Y_test))

#10) 최적(성능좋은 / 오차적은)
from sklearn.linear_model import Ridge
# degree=2, alpha=0.01
# 1. 파이프 라인 만들기
pipe_poly_ridge = Pipeline([
    ('poly', PolynomialFeatures(degree=2,include_bias=False)), # 4
    ('scaler', StandardScaler() ),  #5
    ('ridge', Ridge() ) #6
])

#2. 후보군 파라미터 만들기, {'식별자_파라미터명' : [후보값, 후보값]}
param_grid = {'poly__degree' : [2,3], 'ridge__alpha':[0.001,0.01,0.1,1,10,100]}

#3.k-fold 교차 검증
# kf = kFold(n_splits = "k개의 동일한 폴드로 분할", shuffle=분할시 무작위 섞기, random_state="재현성 확보")
kf = KFold(n_splits =5, shuffle=True, random_state=42)
# 학습 데이터들을 5개로 나누어 4개 학습 하고 1개로 검증 하는 과정을 5번 교차 검증 = 평균오차/ 손실

#4. 그리드서치cv = 교차검증과 다양한 파라미터 자동으로 실행하고 최적 성능 찾기
grid = GridSearchCV( # estimator=진행할 모델, param_grid=파라미터 후보군, scoring='평가지표명', cv=교차 검증  , n_jobs= -1
    estimator=pipe_poly_ridge,
    param_grid=param_grid,
    scoring='r2',
    cv= kf,
    n_jobs=-1

)
#5. 그리드서치로 성능
grid.fit(X_train, Y_train)

#6. 주요 속성
best_model = grid.best_estimator_
print(grid.best_params_)
print(grid.best_score_)

print('r2: ', best_model.score(X_train,Y_train))
print('r2: ', best_model.score(X_test,Y_test))

#11) 서빙, 학습된 모델 저장 하고 다른곳에서 호출
#연구/학습: 코랩(고사양)에서 학습 --> 실제 서버(FAST API) 에서 호출
# 실무: GPU서버 학습 --> 실제 서버(FAST API) 에서 호출

import joblib
#1) 모델 저장한다
# joblib(저장할 모델, 경로)
# model = joblib.dump(best_model,'./day14/fish_model.pkl')

# 1. joblib.load('./day14/fish_model.pk1')
model= joblib.load('./day14/fish_model.pkl')
#2. 불러온 모델로 예측 테스트
import pandas as pd # 임의의 특성 넣어서 예측 무게 찾기
sample = pd.DataFrame({'Length2':[32],'Height':[10],'Width':[4]})

predict = model.predict( sample )
print('예측값/무게:', predict)