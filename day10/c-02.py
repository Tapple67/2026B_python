
# 동적페이지
import requests  # URL 요청 라이브러리
from bs4 import BeautifulSoup # 요청된 URL의 HTML 파싱 라이브러리

#예제2] 동적페이지 크롤링
# 예스24 베스트 셀러 도서 정보 크롤링/ 페이징 처리(반복문)
#1) 크롤링할 주소 가져온다, 정리/분석  categoryNumber=001 국내도서 002 외국 도서 pageNumbe 페이지 번호
#https://www.yes24.com/product/category/daybestseller?categoryNumber=001&pageNumber=2

book_list = []
for page in range(1,4):
    url = f"https://www.yes24.com/product/category/daybestseller?categoryNumber=001&pageNumber=2"
#2 request / URL 요청

    response = requests.get(url)
    #3_ html 파싱
    soup = BeautifulSoup(response.text, "html.parser")
    #4) 특정한 마크업 추출( 책제목, 가격, 저자)
    books = soup.select(".item_info")
    print(books)

    #5 여러개 추출한 마크업에서 특정한 마크업 추출, gd_name, yes_b, info_auth
    for book in books : 
        title = book.select_one('.gd_name').get_text()
        price = book.select_one('.yes_b').get_text()
        auth = book.select_one('.info_auth').get_text().replace("\n","").replace("\r","")

    #6 리스트에 담기
        book_list.append({"제목" : title, "가격": price, "저자": auth})
        
print(book_list)
