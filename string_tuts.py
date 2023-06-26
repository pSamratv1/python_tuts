print('Hello World')

message = "Hello World"
print(message)

# the reason to not use single quote in pyhton:
# new_message = 'Bobby's World'
# It treats the '__'s' as  the end quote for the string  which causes the confusion and causes the error.
# It can be prevented by using the " " or '\'.

new_message = 'Bobby\'s World'
new_message1 = "Bobby's World"
print(new_message)
print(new_message1)

# We can also create a multi-line string using the (triple quotation) or (triple double quotation)
multi_line_message = """This is a multi-line message
where the string can be passed
on a multiple line."""
multi_line_message1 = '''This is also a multi-line message
where the string can be passed on a multiple
line but using a triple single quotation'''

print(multi_line_message)
print(multi_line_message1)

# We can think of string as a string of a  individual characters and we can access the individuals character also,
# so first let's see how we can find how many character are in our string

# len() gives us the length of the items presnt inside the paranthesis

print(len(multi_line_message))
print(len(multi_line_message1))

# and we can access the individual character using the array index method using the square bracket.
# Note that the index always starts from the '0' postion and end at the 'length-1'

print(multi_line_message[0])

# we can also access the range of the character using the ':'
# As [starting_index:stopping_index], Here the starting index is the inclusive but the stopping index is not.
# This is the most common mistake that majority of people makes.

print(multi_line_message[0:29])
# This prints the set of character from 0 index i.e. T of 'This' to the 28 index i.e. e of the message. Once 29 index is reached it stoped.

print(multi_line_message[:29])
print(multi_line_message[29:60])
print(multi_line_message[60:])

# We can as well count the number of characters or string present insiude a string.
# and can use find to find the index of the present item in the string
print(multi_line_message.count('multi'))
print(multi_line_message.find('multi'))
print(multi_line_message.find('m'))


# We can replace the present string with the required string using th e replace method.
# It takes the two parameter: first take wwhat we wamt ot replace and second what we want to replace with
newer_message = "Hello World!"
replaced_message = newer_message.replace('World!', 'Universe')
print("new message: ", newer_message)
print("replaced message: ", replaced_message)

# We can add multiple string and concatinate strings together
greeting = 'Hello'
name = 'Michel'

greeting_message = greeting + name
print(greeting_message) # this outputs 'HelloMichel' and this is not what we wanted so we use the substitute to concat

greeting_message1 = greeting + ', ' + name
print(greeting_message1) # this outputs 'Hello, Michel' similarly

greeting_message2 = greeting + ', ' + name + '. Welcome!'
print(greeting_message2) # this outputs 'Hello, Michel. Welcome!'

# Similary we can use the placeholder for the inputs and use format method for providing the inputs for above problem
formated_message = '{}, {}. Welcome!'.format(greeting,name)
print('formatted message:',formated_message)

# Python 3.6 provides us with the formating using 'f' string formatting for same problem as above.
f_string_formating = f'{greeting}, {name}. Welcome!'
f_string_formating_upper = f'{greeting}, {name.upper()}. Welcome!'
f_string_formating_lower = f'{greeting}, {name.lower()}. Welcome!'

print('f string formating: ',f_string_formating)
print('f string formating upper: ',f_string_formating_upper)
print('f string formating lower: ',f_string_formating_lower)


# finally we can find all the available attributes & method associated with the given variable using the 'dir' method
print(dir(name))

# similarly we can also view the avaible methods ot use with the string methods, we need to use the data_class
print(help(str))
print(help(str.lower))
