# Implicit Conversion - automatic type convert

# Explicit Conversion - manual type convert


# Example 
int_num = 123
flt_num = 1.23 

new_num = int_num - flt_num
print("Value is :", new_num)
print("Data_Type:",type(new_num))


# Explicit Conversion - manual type convert

num_string = '13'
num_int1 = 23
print("Data type of explicit before type Casting",type(num_string))

#manual type convert
num_string = int(num_string)
print("Data type of explicit after type Casting",type(num_string))