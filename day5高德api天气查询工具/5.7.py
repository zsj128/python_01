import json
t=[]
with open('sample.json','r',encoding="gbk")as fp:
    j=json.loads(fp.read())
    print("公司名称:",j['company'])
    print("所在地",j['location'])
    for i in j['employees']:
        print('员工名称:',i['name'],'员工职位:',i['position'])
        t.append(i["salary"])
print("平均工资:",sum(t)/len(t))
