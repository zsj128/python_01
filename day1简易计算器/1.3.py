"""
a =sorted([input() for _ in range(3)])
print("排序后的单词：",a[0],a[1],a[2])
"""
a,b,c=input().split()
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b
print(a,b,c)