#create a new set 

std_id = {2,22,44,55,12}
print('Student ID:', std_id)

#mix data

std = {'Umer',2,'Ali',22,'Khan',804}
print("Student Data:", std)

#empty set
empty_set = set()

#create a empty set
empty = {}

print('Data types', type(empty_set))

#check data type 
print('Data type with data', type(empty))

#Duplicate
numbers = {2,4,2,4,6,8,6}
print(numbers)

# Add item in Python Set
print('Initial Numbers:' , numbers)

numbers.add(32)
print('Updated Set:', numbers)

#remove 
remove_value = numbers.discard(32)
print('After Remove Value: ', numbers)

# union of two sets
#first set 
A = {1,2,3}
#SECOND SET

B = {2,0,4.5}

print('Union String:', A|B)

print('Using union method(): ', A.union(B))