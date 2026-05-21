l=[]
while True:
    print("输入名字")
    name=input()
    l.append(name)
    print("是否继续输入,y/n")
    next=input()
    if next=='n':
        break
l.reverse()
print("反转后的列表：",l)
print("列表中第二个元素出现的次数为：",l.count(l[1]))