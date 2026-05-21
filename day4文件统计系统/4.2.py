t="abcdefgg"
for a,b in enumerate(t):
    if a==t.index(b):
        print((a,b),end='')
        print(b,"出现次数为",t.count(b))
