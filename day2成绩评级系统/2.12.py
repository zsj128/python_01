import random
a = [random.randint(1, 20) for _ in range(20)]
print(a)
a[::2]=sorted(a[::2],reverse=True)
print(a)
a[1::2]=sorted(a[1::2])
print(a)