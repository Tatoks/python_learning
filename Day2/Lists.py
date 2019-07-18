my_greetings='Hello world'
print(my_greetings)
print(my_greetings[0])
print(my_greetings[1])

# Slicing an array
print(my_greetings[0:3])  # Start included, end excluded
print(my_greetings[4:9])

# Negative indexing
print(my_greetings[-1])
print(my_greetings[-2])

# Immutable Strings, Assignment throws error
# TypeError: 'str' object does not support item assignment
# my_greetings[1] = 'E'
print(my_greetings[1])

# Delete
# TypeError: 'str' object doesn't support item deletion
# del my_greetings[1]

# Destroy the entire object
del my_greetings
# NameError: name 'my_greetings' is not defined
# print(my_greetings)

my_greetings='Hello world'
for i in my_greetings:
    print(i)

# Concatenation
print(my_greetings + " " + my_greetings)

for i in range(0, len(my_greetings)):
    print(my_greetings[i], end="")

print("")
for i in range(1, len(my_greetings)+1):
    print(my_greetings[-i], end="")

print()
integer = [1, 2, 3, 4, 5]
print(integer * 3)
print(integer + integer)

#!/usr/bin/env python
# coding: utf-8

# List can have different data type values
my_list = [1, 2.5, "hello world", [1,2,3,4]]
print(type(my_list))
print(id(my_list))
print(my_list)
print(my_list[2][1])
print(my_list[3][3])
print(my_list[0:3])
print(my_list[3][1:3])


# Lists are mutable
# When its values are changed, new list is not created
my_list1 = [1, 2.5, "hello world", [1,2,3,4]]
print(type(my_list1))
print(id(my_list1))
my_list1[0] = 12.5
my_list1[1]= "Oranges"
print(my_list1)
print(type(my_list1))
print(id(my_list1))


# Iterate over sub lists in a list of mixed data types
for i in my_list:
    if type(i)==list:
        for j in i:
            print(j)
    else:
        print(i)


# Concatenate two lists
new_list = my_list + my_list1
print(new_list)

# Reverse Lists
print(new_list[::-1])
revList = list(reversed(new_list))
print(revList)

for i in reversed(new_list):
    print(i, end=", ")

