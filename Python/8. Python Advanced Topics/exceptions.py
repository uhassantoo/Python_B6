# num = 7/0
# print(num)

# print(dir(locals()['__builtins__']))

# Python Expections Handling

try:
    num1 = 10
    num2 = 0
    
    res = num1/num2
    print(res)
except:
    print('Erorr cannot be 0')
    
try:
    evennum = [2,4,8,6]
    print(evennum[3])
except ZeroDivisionError:
    print('Error ')
    
except IndexError:
    print('Index out')