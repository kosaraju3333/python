##  Class creation 
class Circle:
     
    pi = 3.14 # Class object Attribute
    ## Attribute initialises with __ini__ method
    def __init__(self,radius):
        self.radius=radius

    ## Method creation 
    def get_area(self):
        area = self.pi * self.radius ** 2
        return area
    ## Another Method creation
    def get_circumference(self):
        return 2 * Circle.pi * self.radius
    
## Created objects from Class    
circle_1_circum=Circle(4)
print(f"circle_1_circum is: {circle_1_circum.get_circumference()}")
    
circle_1_area=Circle(4)
print(f"circle_1_area is: {circle_1_area.get_area()}")


circle_2_circum=Circle(8)
print(f"circle_2_circum is: {circle_2_circum.get_circumference()}")
    
circle_2_area=Circle(8)
print(f"circle_2_area is: {circle_2_area.get_area()}")

##  Another Class creation 
class Rectangle:
    ## Attribute initialises with __ini__ method
    def __init__(self,length,width):
        self.length = length
        self.width = width

    ## Method creation 
    def get_rect_area(self):
        return self.length * self.width

## Created objects from Class   
rectangle_1_area=Rectangle(12,4)
print(f"rectangle_1_area is: {rectangle_1_area.get_rect_area()} Cm square")

rectangle_2_area=Rectangle(3,3)
print(f"rectangle_2_area is: {rectangle_2_area.get_rect_area()} Cm square")
