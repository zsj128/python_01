class Student:
    school='新余学院'
    banji='一班'
    def __init__(self,name,xingbie):
        self.name=name
        self.xingbie=xingbie
s1=Student('张三','男')
s2=Student('李四','女')

print(s1.name,s2.name)
print(s1.banji,s2.banji)
print(s1.xingbie,s2.xingbie)

print(s1.school)
print(Student.school)

Student.school='江西理工大学'
print(s1.school,s2.school)

