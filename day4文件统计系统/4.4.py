a='abcdefg'
print(a.replace('a',"*"))
b = a.maketrans("abc", "123")
c = ''.maketrans("abc", "123")
d = str.maketrans("abc", "123")
print(a.translate(b))
print(a.translate(c))
print(a.translate(d))