import asyncio
from playwright.async_api import async_playwright

#예제4] 동적 크롤링
#1) 중고나라 홈페이지 제품 크롤링 , url = https://web.joongna.com/search/코카콜라
async def run(): # 함수 정의 
    

    keyword = input(" 중고 제품명: ")
    min_price = input(" 최소가격: ")
    max_price = input(" 최대가격: ")
    #2) async_playwright() 실행하고 끝날때까지 대기 상태
    async with async_playwright() as p:
        #3) 크로미움 실행
        browser = await p.chromium.launch( headless= False)
        #4) 빈 페이지 열기 
        page = await browser.new_page()
        #5) 특정 페이지 이동
        await page.goto( f"https://web.joongna.com/search/{keyword}" )
        #6) 3초 대기상태
        await page.wait_for_timeout(3000)
        #7) 입력받은 값을 웹페이지에 채우기, page.get_by_속성명("속성값") DOM.fill(값) page.get_by_placeholder("최소가격").fill()
        await page.get_by_placeholder("최소 가격").fill(min_price) #html placeholder 이용하여 특정 마크업 식별
        await page.wait_for_timeout(1000) # 1초간 일시 정지

        await page.get_by_placeholder("최대 가격").fill(max_price) #html placeholder 이용하여 특정 마크업 식별
        await page.wait_for_timeout(1000) # 1초간 일시 정지

        #8)특정한 마크업 클릭 이벤트 실행
        await page.get_by_text("적용").click()
        await page.wait_for_timeout(3000)

        #9) 제품사진, 제품명, 제품가격 추출 , href^=  '/시작주소/' 시작주소: 시작주소로 시작하는 모든 주소 식별
        items = await page.query_selector_all("div_group > div > a[href^='/product/']")
        print(items)

        for item in items :
            tilte = await item.query_selector('.typo-body-sm-medium-14')
            tilte = await item.inner_text()
            price = await item.inner if price else  "없음"
            tilte = await item.query_selector('.typo-body-sm-medium-14')
            price =  await item.inner_text() if price else  "없음"
            img = await img.query_selector('img') 
            img = await img.get_attribue('src')if img else" 이미지 없음"

            print(tilte, price, img)
asyncio.run(run()) # 함수 실행
