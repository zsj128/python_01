while True:
    a=input()
    if len(a)!=3:
        print("不是三位数，重新输入")
    else:
        print("个位为：",a[0])
        print("十位为：",a[1])
        print("百位为：",a[2])
        break
"""
print("输入a的值:")
a=input()
print("a的逆序是：",a[::-1])
"""