def p(i):
    b=ord(i)
    if 122>=b>=97:
        c=b-32
    elif 90>=b>=65:
        c=b+32
    else:
        c=b
    return c
a=input()
d=''
for i in a:
    d=d+chr(p(i))
print(d)
    
