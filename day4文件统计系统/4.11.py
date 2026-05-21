s=[]
t='9\n8\n7\n6\n5\n4\n3\n2\n1'
with open('data.txt','w',encoding="gbk")as fp:
    fp.write(t)
with open('data.txt','r',encoding="gbk")as fp:
    for line in fp:
        s.append(int(line.replace('\n','')))
with open('data_new.txt','w',encoding="gbk")as fp:
    for i in sorted(s):
        fp.write(str(i)+'\n')
with open('data_new.txt','r',encoding="gbk")as fp:
    print(fp.read())