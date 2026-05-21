class Student:
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name

s=Student()
s.set_name('李四')
print(s.get_name())