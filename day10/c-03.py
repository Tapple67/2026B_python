# 예제3 동적 페이지 크롤링, 대기/이벤트 존재하는 상태

import asyncio # 비동기 라이브러리
from playwright.async_api import async_playwright # 비동기 동적 페이지 라이브러리

# 1) 크롤링할 페이지 주소 가져온다. 파라미터 분석, ssc= 검색결과 탭메뉴, query = 짱구"

item_list=[]
#2) 비동기 페이지들을 동기화로 제어하는 함수 만들기
#async def 함수명() : # 함수 선언하고 동기화 
async def run():
    url = "https://search.naver.com/search.naver?ssc=tab.image.all&query=짱구"

    # 2-1) 실행
    async with async_playwright() as p : # async with 문법으로 수정
        #2-2) 크로미움 (구글 회사 제공하는 백그라운드용 오픈 소스 브라우저)
        browser = await p.chromium.launch(headless = False)
        #2-3) 현재 실행된 크로미움의 새로운 페이지(빈 페이지 )열기
        page = await browser.new_page()
        #2-3) 빈페이지에 특정한  URL 주소 대입/이동
        await page.goto(url)


# *** asyncio.run( 동기화함수() )***
        for i in range(2):
            await page.wait_for_timeout(3000) # 밀리초 만큼 대기상태 함수
            #await page.evaluate("JS코드삽입")
            #window.scrollTo() : 스크롤 이동 함수
            # document.body.scrollHeight : 현재 페이지의 스크롤 세로높이
            #window.scrollTo(0, document.body.scrollHeight) : 현재 스크롤을 페이지의 가장 하단으로 이동
            await page.evaluate("window.scrollTo( 0 , document.body.scrollHeight )")

            #4) 특정 마크업 가져오기 query_selector 한개 추출 vs ,query_selector_all 여러개 추출
            items = await page.query_selector_all(".tile_item")


            #5) 반복문 이용한 사진 /제목
            for item in items:
                title = await item.query_selector('.info_title')
                title = await title.inner_text() if title else '제목없음' # 특정한 마크업의 사이 텍스트 추출(.innerText)
                img = await item.query_selector('img._fe_image_tab_content_thumbnail_image')
                img = await img.get_attribute('src') if img else '이미지없음' #특정한 마크업의 속성값 추출
                item_list.append( { '제목' : title, "이미지링크" : img} )
    return item_list


asyncio.run(run())

