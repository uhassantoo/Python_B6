# create a function

def greet():
    print('Hellow Python Class')
  
    
#call a function

greet()

# Python arguments

def greet(name):
    print('hellow :',name)


greet('Umer')

def greet(name,age):
    print("hellow:",name,age)

greet('umer',29)

# function add to number\
    
def add(num1,num2):
    sum = num1 + num2
    print('Sum is :', sum)
    
    
#call a function
add(5,4)

#def cal
# def cal(num1,num2):
#     mul = num1* num2

#  Function Return Statement

def find_square(num):
     
    result = num * num 
    return result

#function call
square = find_square(3)
print('Square is :', square)

#  pass

def passfun():
    pass

passfun()

# Function With Default Argumnets

def addnum( a = 10 , b = 10):
    sum = a+b
    print('Sum is :',sum)
addnum(2,3)

def display(firstname = 'UMER' , lastname = 'HASSAN'):
     
    print('First Name :', firstname)
    print('Last Name :', lastname)

display(lastname= 'hELLOW' , firstname= 'Python') 


#Function with Arbitrary Arguments, *args

def find_sums(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
        
    print("Sum is :", result)
    
find_sums(1,2,3,10,15,16)

# Scopes 

def name():
    #local Variable
    msg = 'Hellow Python'
    
    print('Local Scope:', msg)
    
name()
# Call outside the scope
# print(msg)

#decalre globally variable

message = 'Hello python Class'

def names():
    print('Local', message)
    
names()

print("Globally:", message)