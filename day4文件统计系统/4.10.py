s='hello world\n文本文件的读取方式\n文本文件的写入方式'
with open('sample.txt','w',encoding="gbk")as fp:
    fp.write(s)
with open('sample.txt','r',encoding="gbk")as fp:
    print(fp.read())
with open('sample.txt','r',encoding="gbk")as fp:
    print(fp.read(5),len(fp.read(5)))
    print()
with open('sample.txt','r',encoding="gbk")as fp:
    for line in fp:
        print(line,end='')