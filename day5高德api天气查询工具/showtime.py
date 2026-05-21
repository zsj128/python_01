from datetime import datetime 
def show_time():
    now=datetime.now()
    f1=now.strftime("%Y年%m月%d日 %H:%M:%S")
    f2=now.strftime("%A, %B %d")
    return f1,f2