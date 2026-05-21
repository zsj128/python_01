source=[]
while True:
    print("输入分数")
    try:
        source.append(float(input()))
        print("是否继续输入yes/no")
        next=input().lower()
        if next=="yes":
            continue
        elif next=="no":
            break
    except:
        print("输入不合法,重新输入")

print("平均分为：",sum(source)/len(source))
