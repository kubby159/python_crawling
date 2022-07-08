from bs4 import BeautifulSoup as BS

html = '''

<html >

  <body>
    <div>안녕하세요</div>
  </body>
</html>


'''

soup = BS(html,'html.parser')

div = soup.select('div')
print(div[0].get_text(strip=True))