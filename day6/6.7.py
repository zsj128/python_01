class Student:
    school='新余学院'
    def study(self):
        print(f'{self.name}正在学习')

s1=Student()
s2=Student()
s1.name='张三'
s2.name='李四'
print(s1.school)
s2.study()