# Python Classes
# A class is considered a blueprint of objects
#House
#Syntax
# class classname:
#     #class definition

# class car:
#     Name 
#     color
#     brand

# Python objects
#instance of class

# class car:
#     # Attributes
#     name = ''
#     color = ''
#     gear = 0
    

# # create a instance of class
# car1 = car()

# #access attributes

# car1.name = "Honda"

# define a class

class car:
    name = ''
    gear = 0
    color = ''
    
# create a object of class

car2 = car()

#access attributes
car2.gear = 5
car2.name = 'Honda'

print(f"Name : {car2.name}, Gear : {car2.gear} ")


# Create multiple objects of Python Class
 # define class:
class Students:
    std_id = 0
    
#create a two objects of Employee Class
std1 = Students()
std2 = Students()

#access property 
std1.std_id = 1001
print(f"Student ID: {std1.std_id} " )

std2.std_id = 1002
print(f"Student ID: {std2.std_id} " )

# Example
class Room:
    length = 0.0
    breadth = 0.0
  
    
    #method calculate the area
    def cal_area(self):
        print('Area of Room: ', self.length * self.breadth)
  
        
# create a object of class
study_room = Room()
room1 = Room()

#assign the value
study_room.length = 43.5
study_room.breadth = 32.8

room1.length = 40.5
room1.breadth = 29.5

#ACCESS METHOD inside class
study_room.cal_area()
room1.cal_area()

# Python Constructor
class Bike:
     
     def __init__(self , color = '' , name = ''):
         self.color = color
         self.name = name
         
#object
bike1 = Bike()
bike1 = Bike("Honda")


#.............................................

class batch:
      #default constructor
      def __init__(self):
         self.name = 'Batch 6'
         self.color = 'Blue'
         self.std = 20
         
     #method
      def print_name(self):
          print(self.name)
          print(self.color)
          print(self.std)
          
# create a object 

obj = batch()

#access
obj.print_name()


class adds:
     num1 = 0
     num2 = 0
     answer = 0
     
     #constructor
     def __init__(self,first ,second):
         self.num1 = first
         self.num2 = second     
     def display(self):
         print('First Number is : ' , self.num1)
         print('Second Number is : ',self.num2)
         print('Answer is : ' , self.answer)
     def calculate(self):
         self.answer = self.num1 + self.num2
         
#creating a object 
add1 = adds(50,200)

# creating a object of same class
add2 = adds(10,20)

#access

add1.calculate()
add2.calculate()


#display
add1.display()
add2.display()

         
         