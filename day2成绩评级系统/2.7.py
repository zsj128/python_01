while True:
    print("输入学生分数：")
    source=input()
    try:
        float(source)
        if float(source) >= 85:
            print("该学生成绩为等级A，分数为:",source)
            break
        elif 85>float(source)>=60:
            print("该学生成绩等级为B，分数为:",source)
            break
        elif 60>float(source)>=0:
            print("该学生成绩等级为C，分数为:",source)
            break
        else:
            print("输入不合法,重新输入")
    except:
        print("输入不合法，重新输入")