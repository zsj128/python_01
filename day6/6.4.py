import requests
url='https://httpbin.org/delay/1'
try:
    resp=requests.get(url,timeout=2)
    resp.raise_for_status()
    print(resp.raise_for_status())
except requests.exceptions.Timeout:
    print("请求超时")
except requests.exceptions.RequestException as e:
    print("未知错误:",e)