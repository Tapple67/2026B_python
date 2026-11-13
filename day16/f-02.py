# 1. import

import uvicorn

from fastapi import FastAPI

#2. fastapi 객체
app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("f-02:app",host="127.0.0.1", port=8001,reload= True)

#4) 서버 실행: 현재피일py 실행, 여러번 실행 불가

#5 HTTP : 자원 주고 받는 상태구조, REST API: HTTPfh REST구현
#1)FASTAPI 객체 내 get/post/put/delete 메소드 지원
@app.get("/") 
async def index(): # astnc def index(): # async def 함수명() : 비동기 함수 선언
    return "안녕 파이썬 웹" # 반환값
# 코드 작성 후 서버 재설정 없이 "reload=True" 속성으로 자동 서버 반영

#2) 쿼리스트링 : HTTP URL 경로 상에 ? 정의 매개변수
@app.get("/user")
async def user(name, age:int): # 파이썬은 동적 타입이지만 "변수명:타입명" 으로 지정타입 가능
    info = {'name': name, 'age':age, 'msg':"*쿼리통신 성공*"}
    return info # 딕셔너리가 JSON 타입 으로 자동 반환

@app.get("/item/{name}/{age}") # item/유재석/40 -> /item/{변수명}/{변수명}
async def item(name : str, age : int | None = None ): # 파이썬은 동적 타입이지만 "변수명:타입명" 으로 지정타입 가능
    return {name: name, age:age, 'msg':"*쿼리통신 성공*"}
    # 딕셔너리가 JSON 타입 으로 자동 반환

# 4) 본문, HTTP GET/DELETE = > 쿼리/ 경로, HTTP POST/PUT => 쿼리/경로/본문 BODY
@app.post("/product")
async def product(product:dict): # 전달 받은 body 본문(json) 값을 파이썬 dict 타입으로 매핑
    product['msg'] = "*본문통신성공*"
    return product

#요청/테스트에서 body 본문에 {"name":"유재석","age:40"} 으로 보내보기


# http://127.0.0.1:8001/docs



