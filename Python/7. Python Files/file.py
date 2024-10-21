file = open('filehandle.txt', 'r')

for data in file:
    print(data)

# Second way
file = open('filehandle.txt', 'r')
print(file.read())

# File write() Function 
file = open('um.txt', 'w')
file.write('My name is Umer Hassan')
file.write('Python Course')
file.close()

#Another Way
with open ('um.txt', 'w') as new:
    new.write('Hello Python Class')
    
file = open('um.txt', 'a')
file.write('This will add  new line')
file.close()
