class SIE(Exception):
    def __init__(self, length,atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast
try:
    s=input('输入：')
    if len(s)<3:
        raise SIE(len(s),3)
except EOFError:
    print("你输入了一个结束标记EOF")
except SIE as x:
    print('SIE:长度是 %d，至少应是 %d' % (x.length,x.atleast))
else:
    print("没有异常")