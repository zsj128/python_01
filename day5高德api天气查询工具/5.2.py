import os
tolsize,filenum,dirnum=0,0,0
print("输入指定的文件:",end=' ')
d=input()
dirs=os.walk(os.getcwd())
for root, dirs, files in os.walk(d):
    filenum += len(files)
    dirnum += len(dirs)
    for f in files:
        file_path = os.path.join(root, f)
        tolsize += os.path.getsize(file_path)
print("指定的文件夹大小:",tolsize,'B')
print("文件数量:",filenum,"，子文件数量:",dirnum)