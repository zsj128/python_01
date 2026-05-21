d={
    11:{"姓名":"a","性别":"男","联系方式":"187"},
    12:{"姓名":"b","性别":"女","联系方式":"189"},
    13:{"姓名":"c","性别":"男","联系方式":"191"},
    }

def p():
    keys=list(d.keys())
    print("各个学生的信息：")
    for i in range(len(keys)):
        print("学号:",keys[i],"姓名:",d[keys[i]]["姓名"],
            "性别:",d[keys[i]]["性别"],"联系方式:",d[keys[i]]["联系方式"])
    print("\n",end='')


def funtion0(d):
    while True:
        try:
            print("输入查询学生信息的学号：",end='')
            num=int(input())
            if num not in list(d.keys()):
                print("学生信息不存在")
                print("\n",end='')
                break
            if d[num]["性别"]=="男":
                print("学生为男生，",end='')
            else:
                print("学生为女生，",end='')
            print("学号为",num,"，联系方式为:",d[num]["联系方式"])
            print("\n",end='')
            break
        except:
            print("输入错误")
            print("\n",end='')
            break
        

def funtion1(d):
    while True:
        try:
            print("输入要填加的数据:")
            print("学号:",end='')
            id=int(input())
            print("姓名:",end='')
            name=input()
            print("性别:",end='')
            xinbie=input()
            if xinbie not in ["男","女"]:
                print("输入错误")
                print("\n",end='')
                break
            print("联系方式:",end='')
            phone=input()
            if phone.isdigit()==False:
                print("输入错误")
                print("\n",end='')
                break
            print("\n",end='')
            d[id]={"姓名":name,"性别":xinbie,"联系方式":phone}
            p()
            break
        except:
            print("输入错误")
            print("\n",end='')
            break


def funtion2(d):
    while True:
        try:
            print("输入要删除的学生信息的学号:")
            id1=int(input())
            if id1 not in list(d.keys()):
                print("学生信息不存在")
                print("\n",end='')
            else:
                del d[id1]
                print("\n",end='')
                p()
            break
        except:
            print("输入错误")
            break


def funtion3(d):
    while True:
        try:
            print("输入要更新学生信息的学号:")
            id2=int(input())
            if id2 not in list(d.keys()):
                print("学生信息不存在")
                print("\n",end='')
            else:
                print("输入要更新学生信息的哪一部分（姓名1|性别2|联系方式3|）:")
                action=int(input())
                print("输入要更新的信息内容:")
                text=input()
                if action==1:
                    d[id2].update({"姓名":text})
                    print(d)
                if action==2:
                    d[id2].update({"性别":text})
                if action==3:
                    d[id2].update({"联系方式":text})
                print("\n",end='')
                p()
            break
        except:
            print("输入错误")
            break


def funtion4(d):
    while True:
            print("请输入要筛选信息的性别（男1|女2）:")
            sex=input()
            if sex=="1":
                for i in d.keys():
                    if d[i]["性别"]=="男":
                        print("学号:",i,"姓名:",d[i]["姓名"],
                            "性别:",d[i]["性别"],"联系方式:",d[i]["联系方式"])
                print("\n",end='')
                break
            elif sex=="2":
                for i in d.keys():
                    if d[i]["性别"]=="女":
                        print("学号:",i,"姓名:",d[i]["姓名"],
                        "性别:",d[i]["性别"],"联系方式:",d[i]["联系方式"])
                print("\n",end='')
                break
            else:
                print("输入错误，请输入1或2")
                print("\n",end='')

while True:
    print("选择操作，显示所有信息0|查询信息1|输入信息2|删除信息3|更新信息4|按性别筛选信息5|退出6")
    action=input()
    print("\n",end='')
    if action=="0":
        p()
    elif action=="1":
        funtion0(d)
    elif action=="2":
        funtion1(d)
    elif action=="3":
        funtion2(d)
    elif action=="4":
        funtion3(d)
    elif action=="5":
        funtion4(d)
    elif action=="6":
        break
    else:
        print("输入错误")
        print("\n",end='')