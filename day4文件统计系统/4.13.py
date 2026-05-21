import os

def function0(cwd,file):
    for i in os.listdir(cwd):
        if os.path.isdir(os.path.join(cwd,i)):
            function0(os.path.join(cwd,i),file)
        elif i==file:
            print(os.path.join(cwd,i))

def function1(cwd,file):
    dirs=os.walk(cwd)
    for r,d,f, in dirs:
        for ds in d:
            if ds==file:
                print(os.path.join(cwd,ds))
        for fs in f:
            if fs==file:
                print(os.path.join(cwd,ds))

print("输入要查找的文件的目录:",end='')
cwd=input()
print("输入要查找的文件:",end='')
file=input()
print("包含要查找的文件的所有目录:")
function1(cwd,file)

