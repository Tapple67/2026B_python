# 의사결정 결정트리
url = 'https://raw.githubusercontent.com/rickiepark/hg-mldl/master/wine.csv'

import pandas as pd

df = pd.read_csv(url)

X = df[['alcohol','sugar','pH']]
Y = df['class']

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

#1) 결정트리 모델
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
#종속/타깃이 범주형이면 xxxxClassifier, 연속형이면 xxxxRegressor
# 와인의 종류 예측 -> DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train, Y_train)
print("Train Acc : ", model.score(X_train,Y_train))
print("Test Acc : ", model.score(X_test,Y_test))
# Train Acc :  0.9978833942659227
# Test Acc :  0.8738461538461538

#2) 시각화
# import matplotlib.pyplot as plt
# from sklearn.tree import plot_tree
# plot_tree(model,max_depth=2)
# plt.show()

# 3) 규제 : 가지치기( 루트 개수 제한)
model = DecisionTreeClassifier(
    max_depth=3, # 트리의 최대깊이를 3으로 제한하여 복잡도 낮추기
    min_samples_leaf=10, # 리프노드가 가져야할 최소 샘플 수 10개 제한
    criterion="gini", #분할 측정 지표
    random_state=42 # 난수 시드
)

model.fit(X_train, Y_train)
print("Train Acc:",model.score(X_train,Y_train) ) # Accuracy
print("Test Acc:",model.score(X_test,Y_test) ) # Accuracy
# Train Acc: 0.8456802001154512
# Test Acc: 0.8407692307692308
# 규제 없을때 12% 차이가 있지만 규제있을 때 0.5% 차이 줄었다. 성능 좋아졌다.

#4) 타깃/종속 클래스의 불균형(레드/화이트 와인 개수/비율 다르다.)
model = DecisionTreeClassifier(
    max_depth=3, min_samples_leaf=10, criterion="gini", random_state=42,class_weight="balanced") #클래스 빈도에 반비례하여 가중치를 자동 부여하여 불균형 보정

model.fit(X_train,Y_train)
print("Train Acc : ", model.score(X_train,Y_train)) # Accuracy
print("Test Acc : ", model.score(X_test,Y_test)) # Accuracy

# Train Acc :  0.787569751779873
# Test Acc :  0.7946153846153846

#성능이 (5%) 떨어짐 # 과도한 규제 -> 과소적합

#5) 특성 중요도
print(model.feature_names_in_) 
print(model.feature_importances_) #분류 모델에서 예측에 기여한 특성의 중요도 수치

# ['alcohol' 'sugar' 'pH']
# [0.06047705 0.92312892 0.01639403] #sugar 특성이 중요도 수치가 가장 크다

# 6) 앙상블 : 배깅 또는 부스팅 방식으로 복합 모델 구현
# 배깅 앙상블 : 랜덤포레스트 ( 여러 트리모델을 병렬 처리 하여 최적의 모델 찾기)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(
    max_depth=3, # 트리의 최대 깊이 제한 (과적합 억제 )
    class_weight="balanced", # 클래스 불균형 해소 (과적합 억제)
    n_estimators=10,    # 생성할 결정 트리 개수 기본값
    max_features='sqrt',
    random_state=42,
    n_jobs=-1
)
model.fit(X_train,Y_train)
print("Train Acc : ", model.score(X_train,Y_train)) # Accuracy
print("Test Acc : ", model.score(X_test,Y_test)) # Accuracy
# Train Acc :  0.817009813353858
# Test Acc :  0.8007692307692308

#max_features='sqrt' 사용하는 이유: 분류에서 샘플을 사용할때 샘플들을 전체 사용하지 않는다.
# 총 4개 인경우 랜덤으로 4에서 제곱근 하여 2개만 사용. # 전체 샘플 사용시 과적합
# 즉] 전체 ( 숲) 보는 방식이 아닌 무작위로 각기 다른 샘플 사용

print(model.feature_names_in_)
print(model.feature_importances_)
