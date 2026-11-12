# Fast api :HTTTP 비동기 통신 지원하는 프레임워크
#설치 : pip install fastapi uvicorn
#FastAPI 로 unicorn 서버 실행
#1) from fastapu import FastAPI, import uvicorn
from fastapi import FastAPI
import uvicorn

#2)Fast API객체 만들기, 자바: new 클래스() vs 파이썬: 클래스 ()
app = FastAPI()

#3)unicorn 서버 실행 함수 만들기 ,파이썬 main함수 만들기 
#자바 메인 함수 : 메인 스레드 내장 포함하여 프로세스 실행 최초 실행 함수
# 파이썬 if__name__ == "__main__": 해당 py 실행 되면 먼저 진입되는 구역
if __name__ == "__main__":
    uvicorn.run("f-01:app",host="127.0.0.1", port=8000,reload= True)
    
# http://127.0.0.1
#4) 서버 실행 방법 : 현재 unicorn.run 존재하는 파일에서 py 실행
#5) 서버종료 방법 : 해당 서버 터미널에서 ctrl + c or 터미널 닫기
#6)서버 REST API : 127.0.0.1/docs