# reduce() function takes in a function and a list as argument
# new reduced result is returned

from functools import reduce

mylist = [1, 3, 5, 6, 7]
mul = reduce((lambda x, y: x * y), mylist)  # returns product of all elements in mylist
print(mul)
print(type(mul))
