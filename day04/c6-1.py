
#구문 오류: 실행전 오류, 실행 자체 불가능
#런타임 오류: 실행 중 오류, 예외

#예외 처리: 예외를 해결하는 모든 것을

# 조건문 또는 try

#예1] 조건문 예외
input_a = input("정수입력: ")

#int() 정수로 변환 함수
int(input_a)

if input_a.isdigit() : #문자열.isdigit() : 문자열타입의 값이 숫자이면 true
    int(input_a)
else:
    print("정수가 아닙니다.")

#예] try 예외
try :
    int(input_a) # 예외가 발생할것 같은 코드
except:
    print("정수가 아닙니다.")

#예3] pass 키워드, 예외 어떻게 처리할 지 모른경우 일단 넘어가기
try:
    int(input_a)
except:
    pass

#예] else, 예외가 발생하지 않았을 때
try: # 예외가 발생할 가능성이 있는 코드
    int(input_a)
except: # 예외가 발생 했을 때 실행코드
    print("정수가 아닙니다")
else: # 예외가 발생하지 않았을때 실행코드
    print("정수가 맞습니다.")

#예] finally, 예외가 발생하든 발생하지 않든 무조건 실행 코드
try:
    int (input_a)
except:
    print("정수가 아닙니다.")
else:   # java와 차이점
    print("정수가 맞습니다")
finally: # 무조건 실행되는 코드
    print("코드가 끝났습니다.") 

#예6] finally 활용예

try: 
    #open(파일명, 옵션) 파일 불러오기 함수 # w옵션:파일이 없으면 생성
    file = open("info.txt","w") # 일부러 예외 발생
    #try 에서 만약에 예외가 발생하면 발생한 코드이후는 실행안됨. ->except 이동
    #file.close() # 파일.close() : 파일 닫기
    
    예외.발생
except:
    print("오류")
finally:
    file.close()
print(file.closed)
#finally 사용: return함수종료, break반복문 종료 + finally 조합



