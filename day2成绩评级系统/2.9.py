def p(a):
    r=1
    for i in range(2,int(a/2)+1):
        if a%i==0:
            r=0
    return r
s=[]
for i in range(2,101,-1):
    if p(i):
        s.append(i)
print(max(s))