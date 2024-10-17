from math import pi

class Shape:
    def __init__(self,name):
        self.name = name
        
    def area(self):
        pass
    def fact(self):
        return 'I am a two-dimensional shape'
    def __str__(self):
         return self.name

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)
        self.length = length
        
    def area(self):
        return self.length**2
    
    def fact(self):
        return 'Square have each equal angles 90 degres'
    
class Circle(Shape):
     def __init__(self, radius):
         super().__init__('Circle')
         self.radius = radius
         
     def area(self):
         return pi*self.radius**2
     
a = Square(4)
b = Circle(7)

#access

print(b)
print(b.fact())
print(a.fact())
print(b.area())


# Python Operator overloading
#Python Special Function
num1 = 5
num2 = num1.__add__(10)

print(num2)

class Two:
    def __init__(self, x = 0 , y = 0):
        self.x = x
        self.y = y
    
    def __add__(self , other):
        x = self.x + other.x
        y = self.y + other.y
        return Two(x,y)
    
p1 = Two(1,2)
p2 = Two(2,3)

p3 = p1 + p2

print(p3.x , p3.y)

#another overloading

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #overload
    def __lt__(self, other):
        return self.age < other.age
    
a1 = Person('Umer', 29)
b1  = Person('Ali',33)

print(a1<b1)
print(b1<a1)
