import requests

url='https://httpbin.org/delay/1'

try:
    r=requests.get(url,timeout=2)
    r.raise_for_status()
    if r.status_code==200:
        print('状态码为200，请求成功，建立连接')
        print(r.text)
        print('公网IP为:',r.json()['origin'])   
    else:
        print('连接错误')
except requests.exceptions.Timeout:
    print("请求超时")
except requests.exceptions.RequestException as e:
    print("未知错误:",e)




