class Rectangle:
    cont=0
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return self.width*2+self.height*2
    @classmethod
    def create_square(cls,side):
        return cls(side,side)

sq=Rectangle(5,3)

print(f"矩形面积：{sq.get_area()}，周长：{sq.get_perimeter()}")
print(f"正方形面积：{Rectangle.create_square(4).get_area()}，周长：{Rectangle.create_square(4).get_perimeter()}")
