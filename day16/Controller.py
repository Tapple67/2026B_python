#[1] 라우터: 특정 도메인(주소) 묶어 주는 역할
from fastapi import APIRouter
# router = APIRouter(prefix="/공통 URL")
router = APIRouter(prefix="/api")

# [3]다양한 REST API CRUD

# 서비스객체 불러 오기 # from 파일명 import 변수명
from Service import item_service
#1) 전체 조회
@router.get("/items")
async def items():
    #서비스내 함수 호출 
    return item_service.items()

@router.post("/save")
async def save(item:dict):
    return item_service.save(item)

@router.put("/update")
async def update(item:dict):
    return item_service.update(item)

@router.delete("/delete")
async def delete(id:int):
    return item_service.delete(id)