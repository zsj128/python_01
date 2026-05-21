import string
import random
c=string.digits+string.ascii_letters
b=string.punctuation
print("输入密码位数")
n=int(input())
print(random.choice(b)+''.join([random.choice(c) for i in range(n-1)]))