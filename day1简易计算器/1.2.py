
while True:
    print("输入直角边a：")
    a=input()
    print("输入直角边b：")
    b=input()
    if float(a)>0 and float(b)>0:
        a=float(a)
        b=float(b)
        break
    else:
        print("输入错误")

c=(a*a+b*b)**0.5
print(c)