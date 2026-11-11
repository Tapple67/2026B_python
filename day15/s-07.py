import pandas as pd
fish = pd.read_csv("./Fish.csv")

#1) 다중 분류 실습하기 위한 특성 / 타깃(여러개 사용 ) 구분
X = fish.drop(columns=['Species'])
Y = fish['Species']
print(X)
print(Y)

#2) 분리,, stratify = Y 정답지에 학습용과 테스트용 비율 유지 (분류모델 권장)
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

#3) 다항 위한 스케일링
from sklearn.preprocessing import StandardScaler
ss= StandardScaler()
X_train_scaled = ss.fit_transform(X_train) # fit+transform
X_test_scaled = ss.transform(X_test)


#4) 로지스틱 회귀 = 이진 또는 다중에서 자동 선택 된다.
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(C=1.0, max_iter=1000, random_state=42)
model.fit(X_train_scaled, Y_train)
Y_pred = model.predict(X_test_scaled)
print(Y_pred[:3])

print('정답지', model.classes_) # 정답지 종류
Y_pred_proba = model.predict_proba(X_test_scaled)
print('',Y_pred_proba)

import numpy as np
print( np.round(Y_pred_proba[:3], 3) ) #np.round(리스트, 자릿수)

#평가지표
from sklearn.metrics import accuracy_score, classification_report, f1_score, precision_recall_curve, precision_score
#1) 정확도: 전체 예측 건수 중 맞힌 정답의 비율

print(accuracy_score(Y_test, Y_pred )) # 0.8125
#2)정밀도: 예측 한것중 실제로 맞힌 비율
print(precision_score(Y_test,Y_pred, average="macro"))

#3) 재현율: 실제 정답인것 중에 모델이 놓치지 않고 찾아낸비율
print(precision_score(Y_test, Y_pred, average='macro'))

#4) f1 점수/표준
print(f1_score(Y_test, Y_pred, average="macro"))

## 4대 평가지표는 혼동행렬 이용하여 계산한다.
# 혼동행렬 시각화

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
ConfusionMatrixDisplay.from_predictions(Y_test, Y_pred)
# plt.show()


# 파이프라인 구성
from sklearn.pipeline import Pipeline
pipe = Pipeline([
    ('calar', StandardScaler()),
    ('model',LogisticRegression(max_iter=1000, random_state=42))
])

# 하이퍼 파라미터 후보군, "식별자__매개변수명" : [후보값, 후보값]
param_grid = {'model__C': [0.01, 0.1, 1.0, 10.0, 100.0] }

#K폴드 이용한 교차 검증 분할기 (다중분류: StratifiedKFold)
from sklearn.model_selection import StratifiedKFold
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

#그리드 서치
from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(pipe, param_grid, cv=cv, scoring="f1_macro", n_jobs=-1)
grid.fit(X_train, Y_train)
print(grid.best_params_) # 최적의 파라미터
print(grid.best_score_) # 최고의 f1 점수 

best_model = grid.best_estimator_ # 최적의 추정기 /모델 
Y_pred = best_model.predict(X_test) # 최적의 추정기로 예측

print(classification_report(Y_test,Y_pred)) # 파이프라인으로 최적의