# 웹 크롤링: 웹페이지 존재하는 데이터들을 수집 하는 기술
# HTML/CSS 기초 지식
# 파이썬 크롤링 라이브러리 : 
    # 정적 (request/BeautifulSoup), 
    # 동적(seleium, playwright)

# 확인
    #1. 크롤링할 페이지의 도메인주소/robots.txt
    #https://www.jobkorea.co.kr/robots.txt
    #2. 개발자 도구 (f12) -> CTRL+SHIFT+C -> 크롤링 요소 선택 -> 선택자/식별자 확인

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=안양날씨"
#2. requsets 라이브러리로 해당 주소 요청하기

import requests  # URL 요청 라이브러리
response = requests.get(url)
print(response) # 200 정상
print(response.text) # 요청한 주소의 HTML 문자로 반환
#3. 요청 성공했으면 요청한 페이지의 HTML 파싱 하기

from bs4 import BeautifulSoup # 요청된 URL의 HTML 파싱 라이브러리
# BeautifulSoup( 요청한 결과의 내용물, "html.parser")
# BeautifulSoup(response.txt,"html.parser")

soup = BeautifulSoup(response.text,"html.parser") # 요청한 URL 결과 문자열들을 HTML 형식으로 변환
print(soup)

#4. 파싱한 이유 : 특정한 식별자 (마크업) 의 텍스트/ 정보 추출
#soup.select( 선택자 ) : 여러개 추출 # soup.select
text = soup.select_one(".temperature_text")
print(text) # 

#5. 마크업 사이의 텍스트 추출
# 추출한 DOM.get_text() 
print(text.get_text)

