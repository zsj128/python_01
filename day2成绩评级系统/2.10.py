def p(a):
    r=0
    if a%7==0 and a%5!=0 :
        r=1
    return r
s=[]
for i in range(1,101):
    if p(i):
        s.append(i)
print(s)