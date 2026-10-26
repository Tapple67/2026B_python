# 함수? 코드의 집합
    # 값저장 = 변수, 실행 코드저장= 함수
    # 값 여러개 저장 = 리스트/딕셔너리/튜플

#매개변수? 함수를 호출할 때는 괄호 내부에 여러가지를 넣는 변수
#리턴값? 함수를 호출해서 최종적으로 나오는 결과

#def 함수명(매개변수명):
#   실행문

# 값 재사용 = 변수, 코드 재사용 = 반복문(반복패턴존재)/함수(입력/출력)
#회원가입 함수, 회원 목록에서 중복아이디 찾기 = 반복문

#1. 기본적인 함수
def print_3_time():  # 함수 정의/만들기
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_time() # 함수 사용/호출

#vs, 식별자란? p.71 변수/함수명 
for i in range( 0,3,1):
    print("안녕하세요")

#2. 매개변수? 매개( 중매 - 서로 다른 곳에서 연결) , 인수/인자값 -> 매개변수
# 파이썬은 {} 가 아닌 탭 (들여쓰기) 이용하여 구역 구분 
def print_n_times(value,n) :
    for i in range(n):
        print(value)


print_n_times("안녕하세요5",5) # 인수/인자값 란? 함수 호출할 때 매개변수에 전달하는 값
print_n_times("안녕하세요5",3)
# print_n_times("안녕하세요5") # 매개변수는 약속이고 어기면 실행안됨.

# p.278 가변 매개변수
# 조건1: 가변 매개변수가 가장 뒤로 정의한다. # 조건2 : 1번만사용
#def 함수명( 매개변수, 매개변수, *가변매개변수) :
def print_n_times(n,*values):
    for i in range(n):
        for value in values :
            print(value)
        print()
print_n_times(3, "안녕하세요","즐거운","파이썬")
print_n_times(2, "안녕하세요","즐거운",)

# p.279 기본 매개변수, 매개변수에 기본값 대입 형태, 인수/인자 값 생략시 적용
def print_n_times(value, n=2):
    for i in range(n):
        print(value)

print_n_times("안녕하세요") # 안녕하세요 안녕하세요
print_n_times("안녕하세요", 3) # 안녕하세요 안녕하세요 안녕하세요

#p.280
# 기본 매개변수가 가변 매개변수보다 앞에 올때 ,오류
# 가변 매개변수가 기본 매개변수보다 앞에 올때 
# 해결 방안: 키워드 매개변수
print ( "안녕하세요280" ) # 안녕하세요 출력 코드 
print("안녕하세요280", end = "\n") # end 매개변수는 출력후 무엇을 할지 # \n 기본값 = 기본매개변수
print("안녕하세요280", end = " ") # 키워드 매개변수란? 인수 대입시 매개변수명 지정

def print_n_times4(*values, n=2 ):
    # * 매개변수 --> 가변 매개변수 # 매개변수명 =기본값 --> 기본 매개변수
    for i in range(n):
        for value in values: 
            print(value)
        print()
print_n_times4

# p.258 리턴이란? 함수가 종료되면서 반환 되는값
x = 3
y=2
z = x+y #5 # x+y --> def 내가만든공식() : x+y
def myFunc(x,y) : 
    return x+y

#1] 자료 없는 리턴하기, java void
def return_test() :
    print("A 위치 입니다.")
    return # 리턴/함수종료/함수끝 # break 반복문탈출/종료
    print("B 위치 입니다.")
return_test() # B 위치는 출력안됨

#2] 자료와 함께 리턴하기
def return_test2() :
    return 100  # return 값 생략시 None 반환
value = return_test2()
print(value)

def sum_all(start, end):
    output = 0

    for i in range(start,end+1):
        output += i
    return output

print("0 to 100:" ,sum_all(0,100))
print("0 to 1000:", sum_all(0,1000))
print("50 to 100:", sum_all(50,100))
print("500 to 1000:", sum_all(500,1000))


def sum_all(start =0, end =100 , step =1):
    output = 0

    for i in range(start,end+1,step):
        output += i
    return output
print("A" ,sum_all(0,100,10))
print("B" ,sum_all(end=100))
print("C" ,sum_all(end=100,step=2))



def test(a, b=10,c=100):
    print(a+b+c)

test(10 ,20 ,30)

test(a=10,b=100,c=200)