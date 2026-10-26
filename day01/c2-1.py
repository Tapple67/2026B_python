print(type("안녕하세요")) #<class 'str'>
print(type(123))          #<class 'int'>
print(type(1.23))         #<class 'float'>
print(type(True))         #<class 'bool'>
print(type(None))         #<class 'NoneType'>
print(type([]))           #<class 'list'>
print(type({}))           #<class 'dict'>
print(type(()))           #<class 'tuple'> 수정하지 못하는 집합

#86p. 문자열 만들기
print("ABC")
print('ABC')

print("""A
B
C""")           # """ 여러줄 """ 감싼 
print("A'b'c")  #작은 따옴표 출력
print('A"B"C')
print("\"A\'B\nC\tD\\E")

print("안녕"+"하세요")
# print("안녕"+1) # 주의할점 : 문자열과 숫자 연결불가능

#2. *반복연산자

print("안녕"*3)# 안녕안녕안녕
#3. 인덱싱 , 문자열은 배열/리스트 이므로 인덱스 존재한다.
#인덱스란? 0부터 요소들이 저장된 순서,  **음수도 가능** 

print("안녕하세요"[0]) #안
print("안녕하세요"[3]) #세
# print("안녕하세요"[5]) #오류
print("안녕하세요"[-1]) #요
print("안녕하세요"[-3]) #하
# print("안녕하세요"[-6]) #오류

#4. 슬라이싱, 문자열 자르기/일부 추출, [시작인덱스:끝인덱스-1]
print("안녕하세요"[0:2]) # 0~1
print("안녕하세요"[1:3]) # 1~3
print("안녕하세요"[2:4]) # 2~4
# 시작인덱스 생략시 0, 끝인덱스 생략하면 마지막인덱스
print("안녕하세요"[1:]) # 1~  녕하세요
print("안녕하세요"[:3]) # 1~  안녕하

#5. 문자열의 길이, len(문자열)
print(len("안녕하세요")) #5


