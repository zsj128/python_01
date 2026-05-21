class Car:
    color="白色"
    def run(self):
        print(f"一辆{self.color}的车正在行驶")
car1=Car()
car2=Car()
car2.color='红色'
car1.run()
car2.run()

        