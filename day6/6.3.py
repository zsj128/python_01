import requests
url='https://httpbin.org/status/6666'
resp=requests.get(url)
print(resp.status_code)
try:
    resp.raise_for_status()
except:
    print("请求错误")