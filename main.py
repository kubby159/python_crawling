import requests as req

url = ('https://api.imgur.com/3/image?client_id=546c25a59c58ad7')

# image.jpeg
# f =open('image.jpeg', 'rb')
# img = f.read()
# f.close()

with open('image.jpeg','rb') as f:
    img = f.read()

res = req.post(url,files = {
    "image": img,
    "type" : "file",
    "name" : "image.jpeg"
})

print(res.text)



# 200-> 성공
# 400 -> 보내는 사람 잘못
# 500 -> 받는 사람 잘못