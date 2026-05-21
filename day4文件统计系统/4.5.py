import string

def function0(text):
    text_copy=text
    table=''.maketrans("!.?", "|||")
    text1=text.translate(table).split('|')
    total_len=0
    for i in text1:
        if i != '':
            text_copy=text_copy.replace(i,i.lstrip().capitalize())
            total_len+=len(i.capitalize().lstrip().split(' '))
    return text_copy,total_len


def function1(text):
    print("输入文本加密的关键字k:",end='')
    try:
        k=int(input())
        lower_letter_k=string.ascii_lowercase[k:]+string.ascii_lowercase[:k]
        upper_letter_k=string.ascii_uppercase[k:]+string.ascii_uppercase[:k]
        table1=''.maketrans(string.ascii_lowercase,lower_letter_k)
        table2=''.maketrans(string.ascii_uppercase,upper_letter_k)
        text_k=text.translate(table1).translate(table2)
        return text_k
    except:
        print("输入错误，请输入一个整数")


text='hello world! I like python. this is a nice day. right?'
while True:
    print("选操作:输出文本的小写版本1|输出文本的大写版本2|输出文本对应正常的英文格式3|" \
    "统计文本中英文单词的总数4|输出加密后的文本5|退出6")
    text_copy,total_len=function0(text)
    action=input()
    if action not in ['1','2','3','4','5','6']:
        print("输入错误，只能输入1、2、3、4、5、6中的一个")
    else:
        if action=='1':
            print("文本的小写版本:",text.lower())
        if action=='2':
            print("文本的大写版本:",text.upper())
        if action=='3':
            print("文本对应正常的英文格式为:",text_copy)
        if action=='4':
            print("文本中英文单词的总数为:",total_len)
        if action=='5':
            print("加密后的文本为:",function1(text))
        if action=='6':
            break

    