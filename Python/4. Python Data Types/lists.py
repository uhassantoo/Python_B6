ages = [19,22,25,29,40]
print(ages)

name = ['Umer',22, 'hassan']
print(name)

# List Characteristics
#Orderd
#Mutable
# Allow Duplication

lang = ['Python','C++','GO','JAVA','JavaScript']

#Access
print(lang)
#Access through index
print(lang[4])

fruits = ['Apple','Graphes','Orange']

for fruit in fruits:
    print(fruit)
    
print('Lists Methods')

currency = ['Dollar', 'SAR', 'Euro', 'Pound', 'Dinar']
print(currency)

#append Dihram
currency.append('Dihram')
print(currency)


#extend list method

numbers1 = [4,6,8]
number2 = [10,20]

# add items of num1 to number2
number2.extend(numbers1)

print(f'Numbers 1 = {numbers1}')
print(f'Numbers 2 after extend = {number2}')

#insert list method

vowel = ['a','e','i','u']
vowel.insert(3, 'o')
print('List:', vowel)

#count list method 
numbers = [2,44,5,6,8,33,12,44,22,2,44]

count = numbers.count(44)
print('Count of 44:', count)


# index list method
animals = ['cat','tiger','lion','tiger']
#get index of tiger

index = animals.index('tiger')
print(index)

# sort list method 
num = [11 , 3 ,7, 5, 2]
num.sort()
print(num)

# reverse list method 
num1 = [22,44,2,5,8]
print(num1)
num1.reverse()
print('Reverse List: ', num1)