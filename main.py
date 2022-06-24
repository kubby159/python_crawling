# 01234
s = 'apple'

print(s.find('e'))

#array
arr = s.split('p')
print(arr)

#position
#pos
s = '제 생일은 10월 입니다.'
# pos = s.find("생일은 ")
# pos+=4
# print(s[pos:pos+1])


arr = s.split('생일은 ')
s = arr[1]
print(s.split('월')[0])

s = '제 생일은 10월 입니다.'
bd = s.split('생일은 ')[1].split('월')[0]
print(bd)