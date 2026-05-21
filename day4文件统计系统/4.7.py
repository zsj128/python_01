text="""姓名：张三
年龄：39
性别男
职业  学生
籍贯：  地球"""
infor=text.split('\n')
print(infor)
for i in infor:
    print(i[:2].strip("： "))
    print(i[:2],i[2:].strip("： "),sep=':')