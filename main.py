from locale import resetlocale
from bs4 import BeautifulSoup as BS
import requests as req


url = 'https://finance.naver.com/sise/lastsearch2.naver'

res = req.get(url)
soup = BS(res.text, 'html.parser')
stocks =[stock.get_text(strip=True) for stock in soup.select('a.tltle')]
stock_price = [price.get_text(strip=True) for price in soup.select('tr td.number:nth-child(4)')]
stock_ratio = [price.get_text(strip=True) for price in soup.select('tr td.number:nth-child(6)')]

for idx in range(len(stocks)):
    print(f'{stocks[idx]} : {stock_price[idx]} {stock_ratio[idx]}')

