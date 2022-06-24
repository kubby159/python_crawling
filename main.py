import requests as req

res = req.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section')

html = res.text


result = html.split('<span class="value">')[1].split('</span>')[0]
print(result)