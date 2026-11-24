
print('colab에서 파이썬 시작')
#셀 단위 실행 # 노트 모두 실행
#런타임 : 현재 노트가 실행하는 클라우드 PC 상태 #
#런타임중 한번 실행된 셀들은 다른 셀들과 메모리 공유 가능

import torch # 파이토치 라이브러리 호출
device  = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device) #cpu #런타임 유형 변경가능
#2.파이토치는 텐서 객체
import numpy as np
np_data = np.array([[10.0, 20.0, 30.0], [40.0, 50.0, 60.0] ])
x = torch.tensor(np_data, dtype= torch.float32)
print('텐서 shape / dtype:', x.shape, x.dtype)
print(x)

print('-------------------------------------')

print( 'reshape(3, 2)   : ' , x.reshape( 3, 2 ).shape )
print( 'unsqueeze(0)    : ' , x.unsqueeze( 0 ).shape )
print( 'squeeze()       : ' , x.unsqueeze( 0 ).squeeze().shape )
print( 'permute(1, 0)   : ' , x.permute( 1, 0 ).shape )

#4
print( x)
x2 = x.reshape(3,2)
print(x2)
x3 = x.unsqueeze(1)
print( x3 )

#
import torch
sample = torch.tensor([-2.0, 0.0 ,3.0])
print(sample)
#1. 시그모이드 활성화 함수
print( torch.sigmoid(sample))
#2 ReLU 활성화함수
print(torch.relu(sample))

import torch
x = torch.tensor(2.0) # 특성값
y = torch.tensor(1.0) # 타깃값
w = torch.tensor(0.2, requires_grad=True) # 가중치
b = torch.tensor(0.0, requires_grad= True)

learning_rate = 0.1
Y_pred = x * w + b
print(Y_pred)
y_pred = torch.relu( Y_pred )
print(Y_pred)

import torch.nn as nn
criterion = nn.MSELoss() # 손실 함수
loss = criterion(y_pred, y) # 손실 계산
print(loss)

# 역전파
loss.backward()
print(w.grad.item(), b.grad.item() )
#-2.4000000953674316 -1.2000000476837158

# 가중치 기울기 -2.4 편향 기울기 -1.2
# 경사 하강법

with torch.no_grad() :
  #경사하강법 : 가중치 = 기존가중치 -> 1 학습
  #가중치 업데이트(경사하강법) : 가중치 = 기존 가중치 - (학습률*기울기)
  w -= learning_rate*w.grad # 0.2
  b -= learning_rate*b.grad

#가중치/ 편향 기울기 0으로 초기화 ( 다시 계산 하기 위한 )
w.grad.zero_()
b.grad.zero_()

print( f'업데이트 후 -> 새로운 w: {w.item():.4f} | 새로운 b: {b.item():.4f}' )

