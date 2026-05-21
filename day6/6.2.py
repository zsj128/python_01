import requests
url='https://httpbin.org/get'
payload={
    'name':"李四",
    'age':'18',
    'city':'city'
}
res=requests.get(url,params=payload)
print(res.url)
print(res.json())
print(res.text)