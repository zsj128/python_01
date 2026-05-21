"""def p(a):
    r=0
    if int(str(a)[0])**3+int(str(a)[1])**3+int(str(a)[2])**3 == a:
        r=1
    return r
s=[]
for i in range(100,1000):
    if p(i):
        s.append(i)
print(s)"""
"""def p(a):
    r=0
    a=str(a)
    t=0
    for i in range(0,len(a)):
        t+=int(a[i])**len(a)
    if t==int(a):
        r=1
    return r
s=[]
n=int(input())
for i in range(10**(n-1),10**n):
    if p(i):
        s.append(i)
print(s)"""
n=int(input())
for num in range(10**(n-1),10**n):
    if sum(map(lambda i:int(i)**n,str(num))) == num:
        print(num)