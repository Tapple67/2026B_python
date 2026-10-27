import numpy as np

print(np.__version__)

# 3. 넘파이 학습하는 이유 : 1) 데이터 분석 (수치 계산) 2) ML/DL 라이브러리들이 사용

#1] 배열 생성
x = np.array([1,2,3,4]) #1차원 배열
print(x)

x = np.array([[1,2,3], [4,5,6] ]
              )

print(x)

#동적(자동으로 타입 정해주는) 타입 느리다. 넘파이 정적 타입
x = np.array([1, True, "안녕"])
print(x)

y = [2, False, "잘가"] 
print(y)

#2.0 으로 채워진 배열 초기화 , .zeros ((행개수, 열개수))
x= np.zeros((2,3))
print(x)

#3] 1 으로 채워진 배열로 초기화
x = np.ones((2,3))
print(x)

#4] range(시작 인덱스, 끝 인덱스, 단계)

x = np.arange(0,10,2)
print(x)

#5) linspace(시작값, 끝값, 사이범위)
x= np.linspace(0,1,5)
print(x)

# * 넘파이는 리스트 or 튜플 타입의 자료들을 넘파이 타입으로 변환가능
x = np.array((2,3,4))
print(x)

#6]
x = np.array([ [1,2,3], [4,5,6] ]) # 2차원
print(x.shape)

#7] 배열 타입 확인
x= np.array ([1.0, 2.0, 3.0])
print(x.dtype) # float64 # int 64

#8] 배열 차원수 확인
x = np.array([[[1],[2]], [[2],[3]], [[3],[4]]]) #3차원
print(x.size) # 요소/자료 개수 
print(x.ndim) # 차원 개수

#9] 배열의 데이터 타입, np.array(리스트 or 튜플 , dtype = np.타입명)
# np.타입명 (비트수) , 32bit --> 4byte
# np.bool_ : 언더바 주의( 파이썬 bool vs 넘파일 bool_)
# np.bytes : 영문 또는 일부 특수문자 (아스키 코드) 1바이트, 한글 (utf-8) 3바이트
x = np.array([1,2,3], dtype=np.int32)

x = np.array([1.0, 2.0, 3.0], dtype=np.float32)
print(x.dtype)

x= np.array( [True, False, True], dtype=np.bool_)
print(x.dtype)

# x= np.array(['apple','banana','cherry'], dtype=np.byte)
# print(x.dtype)

#10] 타입변환 . .astype()
x = np.array([1.5,2.5,3.5], dtype=np.float32)

y = x.astype(np.int32)
print(y)

# * 타입 지정 이유
# 1] 메모리 효율성/속도/정밀연산
# 2] 텐서플로우/파이토치 라이브러리

numbers = list(range(1, 10+1))

print(list(filter(lambda x: x  %2!=0,numbers)))
print(list(filter(lambda x: 3<= x<7,numbers)))
print(list(filter(lambda x: x**2 <50 ,numbers)))


