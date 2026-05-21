print("输入数字与运算方法:1加法 2减法 3乘法 4除法")
a,b,c = input().split()
a = float(a)
b = float(b)
if c == '1':
    d = a + b
elif c == '2':
    d = a - b
elif c == '3':
    d = a * b
elif c == '4':
    if b != 0:
        d = a / b
    else:
        print("除数不能为0")
        d = None
else:
    print("运算符输入错误")
    d = None

if d is not None:
    print("结果为:", d)