# Identity operator, compares if the address location is same

# is - Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
# is not - Evaluates to false if the variables on either side of the operator point to the same object
#           and true otherwise.

i = 11
k = 10
j = i
if type(i) is int:
    print('i is an integer')
if type(i) is float:
    print('i is a float type')
if i is j:
    print('i and j point to same address')
    print(id(i), id(j))
if i is not k:
    print('i and k do not hold same address')
    print(id(i), id(k))

