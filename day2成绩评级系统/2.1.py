s=["苹果","香蕉","橘子"]
result = None
a=input("请输入水果名称:")
for index, value in enumerate(s):
    if value == a:
        result = index
if result is not None:
    print("水果下标为:", result)
else:
    print("水果不存在")
        