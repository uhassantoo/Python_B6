print('Python is snake')
print('Hello Good Afternoon')

#print with end parameter

# print(object=  end=  file= flush=)

# object - value(s) to be printed
# sep (optional) - allows us to separate multiple objects inside print().
# end (optional) - allows us to add add specific values like new line "\n", tab "\t"
# file (optional) - where the values are printed. It's default value is sys.stdout (screen)
# flush (optional) - boolean specifying if the output is flushed or buffered. Default: False

print('Good Morning ', end='')
print('Today is sunny day')

# Print Concat Strings
print('Hello Programmer' + 'awesome')

#Output Formatting
x = 5
y = 10
print("The value of x is {} and y is {}".format(x,y))

# Python Input 
num = input('Enter a number')

print("You Entered:", num)
print('Data type of num ',type(num))