a = 15
b = 10

'''+ to add a and b
- to subtract b from a
* to multiply a and b
/ to divide a by b
// to floor divide a by b
% to get the remainder
** to get a to the power b'''

#Arithmetic Operator
#addition
print ('Sum is:' , a+b)

#subtraction
print('Sub is : ', a-b)

#multiplication
print('Mul is :', a*b)

#Divison
print('Div is :', a/b)

#floor Divison
print('Floor Div is :', a//b)

#modulo 
print('Modulus is:' , a % b)

#power
print('Power is :', a**b)



#Assignment Operator
# assign 5 to x
x = 5

y = 10



#assign the sum of x and y to x

x += y  # x = x+y

print(x)

#sub
aa = 5
aa -= 3
print(aa)

#mul
aa *=3
print(aa)

#div
aa /=3
print(aa)

#floordiv
aa //=3
print(aa)

#power

aa **=3
print(aa)

#3. Python Comparison Operators

a = 5
b = 2
print (a>b)

print(a<b)

# equal to operator
print('a == b', a == b)

# Not equal to operator
print('a !=b', a!=b)

# Greater than equal to
print('a>=b', a>=b)
# Less than equal to
print('a<=b', a<=b)

# 4. Python Logical Operators

a = 5
b = 6
#Logical AND
print((a>2) and (b>=6))
#print(True and True) #True
#print(True and False) #False

#Logical OR
print((a>2) or (b>=6))
#print(True and False) #True

#Logical Not
print(not True) 

#5. Python Bitwise operators
# & Bitwise Operator

print (10 & 4)
print (10 | 4)
print (10 ^ 4)

# 6. Python Special operators
# is operator

x1 = 5
y1 = 5
x2 = "Python"
y2 = "Python"
x3 = [1,2,3,4]
y3 = [1,2,3]

print(x1 is not y1)
print (x2 is y2)
print(x3 is y3)

# Membership operators

# in 
# not in

msg = 'Hello Mursaleen'
dict = {1 : 'a', 2 : 'b'}

# check Mu is present in msg string
print ('Mu' in msg)

print ('Mu' not  in msg)

print (1 in dict)
print ('a' in dict)