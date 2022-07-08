from bs4 import BeautifulSoup as BS
import requests as req


#1. url를 통해 html 을 가져온다.

url = 'https://search.shopping.naver.com/search/all?query=%EC%95%84%EC%9D%B4%ED%8F%B0%20%EC%BC%80%EC%97%90%EC%8A%A4&cat_id=&frm=NVSHATC'
res = req.get(url)

#2. 가져온 url을 이용해서  text 불러오기
#print(res.text)

soup = BS(res.text,'html.parser')

#3. selector 이용해서 특정 부분의 데이터를 가져오기.
arr = soup.select('ul.list_basis div>a:first-child[title]')
for a in arr:
    print(a.get_text(strip=True))



