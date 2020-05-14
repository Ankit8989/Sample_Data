#To create class Shape and derive  class as Rectangle and Circle

class Shape:
    def __int__(self):
        self.colour='Black'



class Rectangle(Shape):
    def __int__(self):
        super().__init__()  #to call base class
         self.length=0
         self.breath=0

         def get_area(self):
             return self.length*self.breadth


class Circle(Shape):
    def __int__(self):
        super().__init__()
        self.radius=0

         def get_area(self):
             return 3.14*self.radius*self.radius

r1=Rectangle()
r1.length-=5
r1.breadth=4
print("Area:",r1.get_area())
print("Color:",r1.color)

c1=Circle()
c1.radius=10
print("Area:",format(c1.get_area(),"0.2f"))
print("Color:",c1.color)
c1.color="Blue"
print("Color:",c1.color)

