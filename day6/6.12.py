class R:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if 0<age<150:
            self.__age=age
        else:
            print("年龄不合法")
p=R('张三',20)
print(p.get_age())
print(p._R__age)
p.set_age(80)
print(p.get_age())
p._R__age=80
print(p.get_age())
