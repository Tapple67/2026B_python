# #예외 객체란? 발생한 예외 정보 갖는 객체
# #예외 클래스 : Exception(예외 최상위클래스)
# # except 예외 클래명 as 변수명 :
# #as 키워드 : 클래스의 객체변수 생성
# #그외 모든 예외 처리 : 여러개 except 에서 Exception은 항상 마지막에 위치
# # 주의할점 : Exeption 앞에 위치하면 아래 except 예외가 작동 안함 -> 상속 개념
# # raise : 강제로 예외 발생, 주로 CRUD 실패500 의미 
# #p. 383
# list_number = [52,273,32,72,100]

# try:
#     number_input = int(input('정수입력: ')) # 타입 예외
#     print(list_number[number_input]) # 인덱스 예외
#     raise
#     # java: throws new 예외 클래스()
    
# # except Exception as e: # [1] 예외발생시 얘가 다 가져감
# #     print(e)
# except ValueError as e:  #타입 변환 예외
#     print(e)
# except IndexError as e:  # 인덱스 예외
#     print(e)
# except Exception as e: #그외( 최상위) 예외 항상 마지막
#     print(e)


# # 
# a = 10    # 전역 스택
# def 함수():
#     # 단순 전역변수 호출이면 global 생략가능,
#     # 전역변수 수정하면 global 필수
#     global a 
#     a = a+1     #UnboundLocalError
   
#     print(a) # global 없어도 전역스택 가능
#     b =20   # 함수 스택

# 함수()

#반복문
max_value = 0
a = 0
b = 0

for i in range(1,100):
    j =100-i

    if i * j > max_value:
        max_value = i * j
        a = i
        b = j
print(" 최대가 되는 경우: {} * {} = {}".format(a,b,max_value))


#수학적 계산
total = 100

a = total // 2
b = total - a
max_value = a * b

print(f"최대가 되는 경우: {a} * {b} = {max_value}")

# num = [1,2,3,4,5,6,7,8,9]
# output =[[],[],[]]

# output = 
# print(output)