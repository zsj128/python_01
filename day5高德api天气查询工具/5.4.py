a=[]
while True:
    x=input("输入")
    try:
        x=int(x)
        a.append(x)
    except Exception as e:
        print("输入错误")
        print("输出所有",'、'.join(map(str,a)))
        break