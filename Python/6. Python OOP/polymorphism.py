num1 = 1
num2 = 2
print(num1+num2)

a = 2
b = 2
print(a+b)

str1 = 'Python'
str2 = 'Programming'

print(str1+str2)

# // function

print(len('Python'))
print(len(['Python','Java']))

class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f"I am a cat. My name is {self.name} and my age is {self.age} year old")
        
    def makesound(self):
        print('Meowww')
        
class Monkey:
     def __init__(self,name,age):
        self.name = name
        self.age = age
        
     def info(self):
        print(f"I am a Monkey. My name is {self.name} and my age is {self.age} year old")
        
     def makesound(self):
        print('AWWWAAAAA')

cat1 = Cat('Kitty', 2)
monkey1 = Monkey('Shippu', 4)

for animal in (cat1, monkey1):
   animal.makesound()
   animal.info()


