import requests as req


res = req.get('https://webhook.site/a36713b2-b32b-4e00-8057-cae35ae3cf2d?name=hi',headers={
    "User-Agent":  "fastcampus/B1"

})
print(res)