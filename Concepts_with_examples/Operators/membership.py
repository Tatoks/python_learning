# Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples
from typing import List

myList: List[str] = ['apple', 'orange', 'banana']
fruit = 'apple'

# in operator
# Evaluates to true if it finds a variable in the specified sequence and false otherwise.
if fruit in myList:
    print('List holds the fruit: ' + fruit)

# not in operator
# Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.
fruit2 = 'pineapple'
if fruit2 not in myList:
    print('List does not hold the fruit: ' + fruit2)