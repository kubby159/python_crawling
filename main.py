from ctypes import wstring_at
from bs4 import BeautifulSoup as BS
import requests as req
 
url = 'https://finance.naver.com/marketindex/exchangeList.naver'
res = req.get(url)
soup = BS(res.text,'html.parser')


tds = soup.find_all('td')

names = []

for td in tds:
    if len(td.find_all('a')) == 0:
        continue
    names.append(td.get_text(strip=True))

prices = []
for td in tds:
    if 'class'in td.attrs:
        if 'sale' in td.attrs["class"]:
            prices.append(td.get_text(strip=True))



    

# for idx in range(0,len(names)):
#     print(f'{names[idx]} : {prices[idx]}')


names = []

for td in soup.select('td.tit'):
    names.append(td.get_text(strip=True))


prices = []

for td in soup.select('td.sale'):
    prices.append(td.get_text(strip=True))


print(names)
print(prices)