# 사이킷런? 방대한 머신러닝 알고리즘 모델 제공 라이브러리
# pip install scikit-learn

# 머신러닝 목표: 추론 /예측 과정
# 특성


#1] 단순선형회귀
# 1) 판다스로 자료 불러오기
import pandas as pd
df = pd.read_csv('./Fish.csv')
df. info()

# 2) 모델 학습에 사용할 데이터 추출
feature = ['Length2']     # 특성: Length2 (물고기의 대각선 cm)
target = 'Weight'           # 타깃: Weight( 물고기의 무게 g )

#3) x y 구조
x = df[feature] # 2차원
y= df[target] # 1차원

#4) 데이터 분리, 학습용/테스트용 나누기, 학습과 평가 자료 구분
from sklearn.model_selection import train_test_split
# train_test_split('특성', '타깃',test_size='비율', random_state='난수 시드값')

#특성학습자료, 특성테스트자료, 타깃학습자료, 타깃테스트자료 = train_test_split(특성,타깃,test_size=비율)

X_train,X_test,Y_train,Y_test=train_test_split( x , y , test_size=0.2 , random_state=42 )

#훈련세트: 모델에서 규칙을찾는 자료
#테스트세트 모델 학습 후 모델 평가 / 예측 성능 점수 / 지표

#5) 단순 선형회귀 모델
from sklearn.linear_model import LinearRegression
model = LinearRegression()

#6) 모델 학습, model.fit(특성자료, 타깃자료)
model.fit(X_train, Y_train)

#7) 모델 가중치/기울기 확인, model.coef_
print(model.coef_) #[30.43452394]

#8) 모델 편향 (y 절편 ) 확인
print(model.intercept_) # -477.30634978973194

#9) 학습한 모델의 예측, 새로운 x값을 넣어서 y값 구하기. model.predict(2차원 특성 자료)
print( model.predict([[30]]) )

# *) 시각화
import matplotlib.pyplot as plt
plt.scatter(X_train,Y_train)
plt.plot([0,100], model.predict([[0],[100]])) # 회귀선 : 임의의 최솟값/ 최댓값
plt.scatter([30],model.predict([[30]]),color="red")


# plt.show()
#11) 문제점
# x,y 가 직선 관계이며 실 자료들은 꼭 비례 증가가 아닐 수 있다. 
# 해결 : 다항 회귀 로 확장하여 특성 추가 한다.


#12) 모델 평가 , 테스트용 자료 사용
# 평균 제곱근 오차 계산 
Y_pred = model.predict(X_test) # 테스트용 특성을 넣어 테스트 예측 결과
import numpy as np # sqrt 제곱근 넘파이 함수 사용.
from sklearn.metrics import mean_squared_error # 평균 오차(정답지와 예측 )
rmse = np.sqrt(mean_squared_error(Y_test, Y_pred))
print("rmse", rmse)

# 모델이 실제 무게와 얼마나 틀렸는지 평균 오차


# 결정 계수( R SCORE ) : 타깃 데이터의 전체 변동성 대비 모델이 얼마나 잘 설명하는지 0~1
from sklearn.metrics import r2_score # 결정 계수
r2 = r2_score(Y_test,Y_pred) # 정답지와 예측값
print(r2)


