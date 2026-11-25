

import pandas as pd

url = 'https://raw.githubusercontent.com/rickiepark/hg-mldl/master/wine.csv'
df = pd.read_csv( url )

X = df[ ['alcohol', 'sugar', 'pH'] ] #
Y = df['class']           # (0:레드와인, 1:화이트와인)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train_scaled = ss.fit_transform( X_train )
X_test_scaled = ss.transform( X_test )

#딥러닝 하기 위한 파이토치
print(X_train.shape)
print(Y_train.shape)
# torch.tensor( 자료 , dtype=torch.타입비트수 ) : 텐서타입으로 변환
import torch
X_train = torch.tensor(X_train_scaled, dtype = torch.float32)
X_test = torch.tensor(X_test_scaled, dtype = torch.float32)
#특성과 타깃의 차원 수 일치화
Y_train = torch.tensor( Y_train.values, dtype=torch.float32).unsqueeze(1)
Y_test = torch.tensor( Y_test.values, dtype=torch.float32).unsqueeze(1)

print( X_train.shape )
print( Y_train.shape )

#2) 신경망 ANN 레이어 컨테이너 설정
import torch.nn as nn
model = nn.Sequential(
    # nn.Linear(피처수,파생피처수)
    nn.Linear(3, 16),
    nn.ReLU(), # 활성화 함수 음수값은 0으로 양수값을 유지시킨다. 유의미한 값은 통과
    # nn.Linear(앞전 노드의 피처수 , 결과수)
    nn.Linear(16, 1), # 출력층
)

#3) 손실함수:
crierion = nn.BCEWithLogitsLoss()

#4) 옵티마이져:optimizer = optim.AdamW(model.parameters(), lr=0.01)
import torch.optim as optim
optimizer = optim.AdamW(model.parameters(), lr=0.01)

#5) 에포크 ( 학습 수) 단위 학습 (순전파 -> 역전파)
for epoch in range(1000) :
  model.train() # 5-1 학습 한다.
  optimizer.zero_grad() # 5-2 이전 에포크의 계산된 기울기 초기화
  logits = model(X_train) # 순전파 5-3 학습 자료 넣어서 학습
  loss = crierion(logits, Y_train) # (손실) 5-4 정답과 비교하여 손실계산
  loss.backward() # (역전파) 5-5각 가중치에 기울기를 계산
  optimizer.step() #(업데이트) 5-6 가중치 반영


  #==========================확인용============================
  if epoch % 100 == 0:
    print(epoch, ":loss", loss.item())

  #6) 모델 평가. model.train()학습모드 , model.eval() 평가 /추론모드
  model.eval() # 추론/평가 모드로 전환
  with torch.no_grad(): # 기울기 저장 안함
    train_pred = (torch.sigmoid(model(X_train)) >= 0.5).float()
    test_pred = (torch.sigmoid(model(X_test)) >= 0.5).float()
    # train_acc = (train_pred == Y_train).float().mean()
    # test_acc = (test_pred == Y_test).float().mean()

#7) f1-score
from sklearn.metrics import f1_score
print( f1_score( Y_train.numpy() , train_pred.numpy() , average='macro') )
print( f1_score( Y_test.numpy() , test_pred.numpy() , average='macro'))

"""#[2] 신경망 DNN 이용한 이진 분류

"""

import pandas as pd
url = 'https://raw.githubusercontent.com/arunk13/MSDA-Assignments/master/IS607Fall2015/Assignment3/student-mat.csv'
df = pd.read_csv( url, sep=';' )
X = df[ ['studytime', 'absences', 'G1', 'G2'] ]
Y = df['G3']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=0.2, random_state=42 )

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train_scaled = ss.fit_transform( X_train )
X_test_scaled = ss.transform( X_test )


# 1) 딥러닝 하기 위한 파이토치 특성과 타킷 차원 일치화

X_train = torch.tensor( X_train_scaled , dtype=torch.float32 )
X_test = torch.tensor( X_test_scaled , dtype=torch.float32 )
Y_train = torch.tensor( Y_train.values, dtype=torch.float32).unsqueeze(1)
Y_test = torch.tensor( Y_test.values, dtype=torch.float32).unsqueeze(1)


# 2) 신경망 DNN 레이어 컨테이너 설정
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(4, 32), # 학습할 특성의 수로 입력층 시작
    nn.ReLU(), # 활성화 함수
    nn.Dropout(p=0.2), #매 순전파 마다 은닉층에 20% 무작위 비활성화
    nn.Linear(32, 16), # 앞전 레이어 32노드수 따라서 다음 노드수 설정
    nn.ReLU(),nn.Dropout( p=0.2 ),
    nn.Linear(16, 8), # 앞전 레이어 16노드수 따라서 다음 노드수 설정
    nn.ReLU(),nn.Dropout( p=0.2 ),

    nn.Linear(8,1) # 출력층 이므로 1 노드로 끝낸다.

)
# 3) 손실함수: MSELoss()
crierion = nn.MSELoss()
# 4) 옵티마이저 ; optimizer = optim.AdamW( model.parameters(), lr=학습률)
import torch.optim as optim
optimizer = optim.AdamW( model.parameters(), lr=0.01)
# 5) 에포크(학습수) 단위 학습( 순전파 -> 역전파)
for epoch in range(1500) :
  model.train() # 1)학습모드 실행 , 필수!
  optimizer.zero_grad() #2) 이전 학습에 사용된 기울기 0으로 초기화
  logits = model(X_train) #3) 순전파/ 학습
  loss = crierion( logits, Y_train) # 4) 손실 계산 #(예측값, 정답지)
  loss.backward() #5) 역전파 : 앞전에 오차 이용한 가중치와 편향 계산
  optimizer.step() #6) 업데이트/ 변경된 파라미터 (가중치/편향)반영
 # ==================================================================  #
  if epoch % 100 == 0 :
       print( epoch,": loss: ", loss.item() )

# 6) 모델 평가. model.train()학습모드 , model.eval() 평가/추론모드
model.eval()
with torch.no_grad() :
    train_pred = model( X_train ) # 회귀 이므로 별도의 추가 코드 없음
    test_pred = model( X_test )
from sklearn.metrics import r2_score
print( r2_score( Y_train.numpy(), train_pred))

# 7) 추론
new_students = [ [4, 0, 16, 17 ],[1, 10, 7, 5 ] ]
new_train = torch.tensor( ss.transform( new_students ), dtype=torch.float32 )

with torch.no_grad():
  new_pred = model(new_train)
print(new_pred[0].item()) # 첫번째 학생의 G3 점수 예측
print(new_pred[1].item()) # 두번째 학생의 G3 점수 예측