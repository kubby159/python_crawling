from bs4 import BeautifulSoup as BS
import requests as req


#1. url를 통해 html 을 가져온다.

url = 'https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb'
res = req.get(url,headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})

#2. 가져온 url을 이용해서  text 불러오기
#print(res.text)

soup = BS(res.text,'html.parser')

#3. selector 이용해서 특정 부분의 데이터를 가져오기.
# list comprehension

arr = soup.select('div.pname p')
for a in arr:
    print(a.get_text(strip=True))