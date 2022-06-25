import requests as req
import re



url = 'https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'

res = req.get(url)
body = res.text

# DOT (.) 은 엔터를 미포함.
# re.DoTALL : 엔터를 포함한다.
# ? 를 이용해서 가장 좁은 범위의 데이터를 가져옴.
r = re.compile(r'h_lst.*?blind">(.*?)</span>.*?value">(.*?)</', re.DOTALL) # 정규식표현을 작성한다.

captures = r.findall(body)

print(captures)

print('----------')
print('환율 계산기')
print('----------')


for c in captures:
    print(f'{c[0]} : {c[1]}')





print()
usd = float(captures[0][1].replace(',',''))
won = int(input("달러로 바꾸길 원하는 금액(원)을 입력해주세요."))

dollar = int(won/usd)  
print(f'{dollar} 달러 환전되었습니다.')