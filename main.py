import re


# A B C F

s = "이 영화는 F등급 입니다"
# print(s.split('이 영화는')[1].split('등급')[0])
# print(re.match(r'이 영화는 [ABCF]등급 입니다',s))

# regex 사용
# print(s.split('이 영화는 ')[1].split('등급')[0])
print(re.findall(r'이 (..)는 ([ABCF])등급 입니다',s))