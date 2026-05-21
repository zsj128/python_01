import requests

url='https://restapi.amap.com/v3/weather/weatherInfo'
KEY='3f16c60b891bc35d7e2692a707ba02b8'

def functino1(KEY):
    try:
        print('输入要查询天气的城市:',end='')
        city=input()
        r=requests.get(url,{
                'city':city,
                'key':KEY,
                'extensions':'base',
                'output':'json'
            })
        r.json()['status']
        print('查询今天天气（输入1）|查询今天及未来三天的天气（输入2）:',end='')
        action=input()
        if action not in ['1','2']:
            print('查询方式只能输入1或2')
            return
        return city,action
    except:
        print("无法查询到该城市的天气信息")
        return

def function0(city,action,KEY):
    try:
        if action=='1':
            option={
                'city':city,
                'key':KEY,
                'extensions':'base',
                'output':'json'
            }
            r=requests.get(url,params=option)

            r1=r.json()['lives']
            r1[0]["weather"]
            print(f'---{city}今天天气---')
            print(f'天气:{r1[0]["weather"]}')
            print(f'温度:{r1[0]["temperature"]}')
            print(f'风向:{r1[0]["winddirection"]}')
            print(f'风强:{r1[0]["windpower"]}')

    except:
        print('请求错误')
    try:
        if action=='2':
            option={
                'city':city,
                'key':KEY,
                'extensions':'all',
                'output':'json'
            }
            r=requests.get(url,params=option)

            r2=r.json()['forecasts'][0]['casts']
            r2[0]['dayweather']
            print(f'{city}今天及未来三天的天气为:')
            print(f"{r2[0]['date']}:白天天气:{r2[0]['dayweather']},晚上天气:{r2[0]['nightweather']},白天温度:{r2[0]['daytemp']},晚上温度:{r2[0]['nighttemp']}")
            print(f"{r2[1]['date']}:白天天气:{r2[1]['dayweather']},晚上天气:{r2[1]['nightweather']},白天温度:{r2[1]['daytemp']},晚上温度:{r2[1]['nighttemp']}")
            print(f"{r2[2]['date']}:白天天气:{r2[2]['dayweather']},晚上天气:{r2[2]['nightweather']},白天温度:{r2[2]['daytemp']},晚上温度:{r2[2]['nighttemp']}")
            print(f"{r2[3]['date']}:白天天气:{r2[3]['dayweather']},晚上天气:{r2[3]['nightweather']},白天温度:{r2[3]['daytemp']},晚上温度:{r2[3]['nighttemp']}")

    except:
        print('请求错误')

if __name__=="__main__":
    a=list(functino1(KEY))
    print(a)
    if a!=None:
        function0(a[0],a[1],KEY)