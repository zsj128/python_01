import requests
request=requests.get('https://httpbin.org/get')
print(request)
print(request.status_code)
print(request.text)
print(request.headers)