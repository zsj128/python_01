PI=3.14

class Shape:
    def get_area():
        return 0
    
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def get_area(self):
        return self.side**2
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def get_area(self):
        return (self.radius**2)*PI
    
def calculate_total_area(a,b):
    return a.get_area()+b.get_area()

c=Circle(2)
s=Square(4)
print(f"总面积:{calculate_total_area(c,s):.2f}")