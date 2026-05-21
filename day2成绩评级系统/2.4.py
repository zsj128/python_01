l=[1,-2,3,-4,5,-6]
def s1(a):
    return a>0
def s2(a):
    return a*2
l=list(filter(s1,l))
print(list(map(s2,l)))
