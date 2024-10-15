#define a superclass (PARENT)
# class superclass:
#     #attributes and methods
    
#inheritance
# class sub_class(superclass):

class Animal: #superclass
    #attributes
    name = ""
    def speak(self):
        print('Animal Speaking')
    def eat(self):
        print('I can eat')
class Cat(Animal): #subclass
    def display(self):
        print('My name is', self.name)
    def meow(self):
        print('Cat Meow')
#create an object of subclass
tommy = Cat()

#access  from superclass

tommy.name = 'Meowwww'
tommy.speak()
tommy.eat()
# access from subclass
tommy.display()
tommy.meow()


class Sufa:
    name = ""
    color = ''
    brand = ''
    def shirts(self):
        print('Sweat Shirts')
    def caps(self):
        print('Women Caps')

class Sufasons(Sufa):
    
    #overirde the method shirts()
    def shirts(self):
        print('Sufasons shirts and caps')
        
#create a object
a = Sufasons()

a.shirts()

#super() function in Inheritance

class Thesufa(Sufa):
    #overide method 
    def shirts(self):
        #call the shirts method of superclass
        super().shirts()
        
        super().caps()
        
        print('The sufa boys and girls shirt')
        
#create a object
b = Thesufa()

#access 
b.shirts()

'''Inheritance Types
There are 5 different types of inheritance in Python. They are:

Single Inheritance: a child class inherits from only one parent class.
Multiple Inheritance: a child class inherits from multiple parent classes.
Multilevel Inheritance: a child class inherits from its parent class, which is inheriting from its parent class.
Hierarchical Inheritance: more than one child class are created from a single parent class.
Hybrid Inheritance: combines more than one form of inheritance.'''


# Multiple Inheritance

class Birds:
    def birds_info(self):
        print('Birds Details')

class tiger:
    def tiger_info(self):
        print('King of Jungle')
        
class baby(Birds,tiger):
    print('Hello')

#create a object
b1 = baby()

#access
b1.birds_info()
b1.tiger_info()

#Multilevel Inheritance
class SuperCls:
    def super_method(self):
        print('Supercls method called')
        
#define a classs that derived from Supercls
class derivedcls1(SuperCls):
    def m1(self):
        print('M1 method called')
        
class derivedcls2(derivedcls1):
    def m2(self):
        print('M2 method called')
        
#create a object
d2 = derivedcls2()

d2.super_method()
d2.m1()
d2.m2()