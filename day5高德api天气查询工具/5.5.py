class error0(Exception):
    def __init__(self,):
        Exception.__init__(self)
        print("输入错误，请输入0-100中的数")

try:
    print("输入成绩: ",end='')
    n=int(input())
    if n not in range(0,101):
        raise error0
    else:
        print("输入的成绩正常:",n)
except ValueError as e:
    print("输入错误，要求输入正数")
except error0 as e0:
    e0