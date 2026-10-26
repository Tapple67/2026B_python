# p.317
# 튜플이란? 여러자료들을 저장하는 리스트와 비슷한 자료형

#특징: 초기화 이후 수정 불가능
#사용처 : 읽기 모드용, 수정 없는 자료( 리스트보다 성능좋음)
#(요소,요소,요소)


#1. 튜플 선언
tuple_test = (10,20,30)

#2. 요소값 호출
print (tuple_test[0], tuple_test[2])

#3. 요소값 수정
# tuple_test[0] = 40  # 수정x

#4. 요소하나인 경우
tuple_test2 = (273) #뒤에, 쉼표 없으면 일반값 취급
print(tuple_test2)

#5. 튜플은 소괄호 생략해도 된다.
(a,b) = (10 , 20)
print(a, b)
a, b = 10, 20
print(a, b)

print(a,b)

# - 스왑 / 구조분해 
a, b = b , a # a에 b값 대입, b에 a값 대입

print(a,b)
# - 리액트(js)에서 비슷한 문법 존재 -> 구조분해( useState, props)

c, d = [30,40]
print(c,d)


# 6. 함수/ 연산 결과는 항상 1개
def test():
    return 10, 20 #결과는 1개(10과 20 튜플로 묶은 튜플 1개)

#7. 콜백함수 : 함수 그 자체를 매개변수를 전달하여 전달받은 곳에서 전달받은 함수 호출
# 리액트: onClick( 회원가입() ) [x] ----> onClick( 회원가입 ) [o]
def call_10_items( func ) : # 값 대신에 함수 받기 
    func()
def print_hello() : 
    print( "안녕하세요")

#call_10_items( print_hello() )  #  print_hello() 함수 실행 결과값 전달 
call_10_items( print_hello )    #  print_hello 함수 (그자체)정보 전달 

# java : 리스트.stream.forEach( ), 리스트.stream.map( ), 리스트.stream.filter( ) 
# react : 리스트.forEach( ) , 리스트.map( ) , 리스트.filter( )
#python: for x in 리스트 , map(코드, 리스트) , filter(코드, 리스트)

#forEach 단순 반복, map 반복,반환(return 있다.) , filter 반복+ (참이면)반환

def power(item) :
    return item * item
def under_3(item):
    return item < 3

list_a = [1,2,3,4,5]
print(map(power,list_a)) # map

print(list(map(power,list_a))) # map

print(filter(under_3, list_a)) # py filter

print(list(filter(under_3, list_a))) # py filter

# p.324 람다 (화살표함수)? 코드 줄이기
#lambda 매개변수 : 리턴값
#JAVA: () => {}
#JS: () => {} 

power = lambda item : item*item
output_a = map(power, list_a)
#인라인 람다 
output_a = map(lambda item : item*item,list_a)

#---------------------------------------------------
# def mul(*values):
#     q=1
#     for value in values:
        
#         q = q * value
#     return q

# print(mul(5,7,9,10))

# def func(vaA =10, vaB=20, *va):
#     return "pass"
# print(func(1,2,3,4,5))

# def func2(*va, vaB=20, vaA =10):
#     return "pass"

# print(func2(1,2,3,4,5))

# def func3(*va, vaB, vaA):
#     return "pass"

# print(func3(1,2,3,4,5))

print("---------------------")
최대인원 = 10
최소인원 =2
memo = {}

def func(rest,min):
    key = str([rest,min])

    if key in memo:
        return memo[key]
    if rest < 0:
        return 0
    if rest ==0:
        return 1
    
    result = 0
    for i in range(min,최대인원+1):
        result += func(rest-i,i)
        
        
    memo[key]=result
    return result

print(func(100,최소인원))