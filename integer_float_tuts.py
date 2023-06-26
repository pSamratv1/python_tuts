# There are two types of numeric data types in python 1. Integer 2. Float
num = 2
print(type(num))

number_1 = 3.1
print(type(number_1))


# There are the various of operation associated with these data types
# Arithematic operations
# Addidtion (+): This operator adds the operands
# Subtraction (-): This operator subtracts the operands
# Multiplication (*): This operator multiplies the operands
# Divison (/): This operator divides the operands
# Float Division (//): This operator gives yhe quotient of the operand division
# Exopnential (**): This operator is the power of the operands
# Modulus (%): This operator gives the remaiinder of the operand division

num_1 = 3
num_2 = 2

print(num_1 + num_2)    # (3+2) = 5
print(num_1 - num_2)    # (3-2) = 1   
print(num_1 * num_2)    # (3*2) = 6
print(num_1 / num_2)    # (3/2) = 1.5
print(num_1 // num_2)   # (3**2) = 1
print(num_1 ** num_2)   # (3//2) = 9
print(num_1 % num_2)    # (3%2) = 1


## We can also define the priority of operation using the BODMAS rule in Python using the parnathesis
print(3*2+1)
print(3*(2+1))

# We can also perform the increment and decrement operation using the prefix operands like
num_3 = 1
num_3 += 10
print(num_3)

# There are the various methods and operation associated with the integer and float some of them are as follow
negative_num = -3
positive_num = abs(negative_num) # this method removes the sign associated with the number
print(positive_num)

float_num = 3.75
int_num = round(float_num)
float_num_to_nearest_decimal = round(float_num,1)
print(int_num)
print(float_num_to_nearest_decimal)

# Comparison operator
# Equal to (==): This compares whether the opreands are equal
# Not equal (!=): This compares whether the operands are not equal
# Greater than(>): This compares whether the first operands is greater than second operands
# Less than(<): This compares whether the first operands is less than second operands
# Greater than or equals to (<=): This compares whether the first operands is greater than or equals to second operands
# Lesser than or equal to (>=): This compares whether the first operands is lesser than or equals to second operands


# Some time we come with unique problem that the variable holds the integer value but the adding is not possible like in below

str_num_1 = '100'
str_num_2 = '200'
print(str_num_1+str_num_2) # This gives the output '100200' instead of '300'.

#we can solve this using the type casting.
str_num_1=int(str_num_1)
str_num_2=int(str_num_2)
print(str_num_1+str_num_2)