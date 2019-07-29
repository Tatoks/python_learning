#!/usr/bin/env python
# coding: utf-8

#A dictionary is a collection which is unordered, changeable and indexed.
#In Python dictionaries are written with curly brackets, and they have keys and values.

# Key Value Pairs
mydict = {'a': 'apple',
          'b': 'ball',
          'c': 'cat',
          'd': 'dog'}
print(mydict)
print(mydict['a'])

mydict['a'] = 'Avacado'  # update value for key 'a'
print(mydict)

del mydict['b']  # Delete 'b' key value pair
print(mydict)

# Below line deletes entire dictionary
# del mydict
# print(mydict)

for i in mydict:
    print(i, ":", mydict[i])

print("-------Use Items() method-------")
for key, value in mydict.items():
    print(key, value)

# Print length of dictionary
print(len(mydict))

# Multi dimensional dictionaries

students = {101: {'name': 'John', 'maths': 50, 'chemistry': 56, 'physics': 75},
            102: {'name': 'Steve', 'maths': 66, 'chemistry': 89, 'physics': 59},
            103: {'name': 'Peter', 'maths': 88, 'chemistry': 78, 'physics': 86},
            104: {'name': 'Ben', 'maths': 99, 'chemistry': 76, 'physics': 99}
            }

for student in students:
    print(students[student]['name'], end=",")

print()
print('-----------------------------------------')

for key, value in students.items():
    print(key, end=":")
    for k, v in value.items():
        #         print(k, v, end=',')
        print(v)
    print("")
