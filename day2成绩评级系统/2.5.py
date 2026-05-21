names=['a','b','c']
sources=[61,90,50]
list(zip(names,sources))
def s(a):
    return a[1]>=60
print("合格的学生和成绩为：")
result=0
for name, source in filter(s, zip(names, sources)):
    result+=1
    print(name, source)         
print("合格的学生人数为：", result)