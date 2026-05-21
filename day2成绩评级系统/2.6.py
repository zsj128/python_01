names=['a','b','c']
sources=[[60,70,40],[80,85,99],[70,90,66]]
names=[]
sources=[]
source_1=[]
source_2=[]
source_3=[]
"""while True:
    print("输入学生姓名：")
    name_iuput=input()
    names.append(name_iuput)
    print("输入学生语文成绩：")
    sources.append(float(input()))
    print("输入学生数学成绩：")
    sources.append(float(input()))
    print("输入学生英语成绩：")
    sources.append(float(input()))
    print("是否继续输入（y/n）：")
    next=input()
    if next=="n":
        break"""

for name, source in list(zip(names, sources)):

    print(name,"学生的语文成绩为：",source[0],"，数学成绩为：",source[1],"，英语成绩为：",source[2],
          "，总分为：",sum(source),"平均分为：",format(sum(source)/3,'.2f'))
    source_1.append(source[0])
    source_2.append(source[1])
    source_3.append(source[2])

    if sum(source)/3>=85:
        print(name,"学生成绩优秀")
    elif 85>sum(source)/3>=60:
        print(name,"学生成绩合格")
    else:
        print(name,"学生成绩不合格")

print("语文第一为学生",names[(source_1.index(max(source_1))-1)],"，成绩为",max(source_1))
print("数学第一为学生",names[(source_2.index(max(source_2))-1)],"，成绩为",max(source_2))
print("英语第一为学生",names[(source_3.index(max(source_3))-1)],"，成绩为",max(source_3))