def s(a):
    return a%2!=0
def s1(a):
    return a%2==0
print(list(filter(s,range(11))))
print(list(filter(s1,range(11))))