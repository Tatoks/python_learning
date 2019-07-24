# These are unordered sets

my_empty_dictionary = {}  # Creates an empty dictionary
my_empty_set = set() # Creates an empty set
print(my_empty_set)
print(type(my_empty_set))

my_set = {100, 200, 20, 12, 4, 'hello'}
print(type(my_set))
print(my_set)

my_set.add(200)
my_set.add(200)  # duplicate values are not added

print(my_set)

print('---------------------------------------------------')
set1 = {1, 2, 3, 4, 5, 12}
set2 = {1, 3, 5, 6, 7, 8, 9, 11}
print('Union:', set1.union(set2))
print('Operator Union: ', set1 | set2)

print('intersection:            ', set1.intersection(set2))
print('Operator intersection:   ', set1 & set2)

print('difference:          ', set1.difference(set2))
print('Operator difference: ', set1 - set2)
print('symmetric_difference:            ', set1.symmetric_difference(set2))
print('Operator symmetric_difference:   ', set1^set2)

print('isdisjoint:  ', set1.isdisjoint(set2))
print('issubset:    ', set1.issubset(set2))
print('issuperset:  ', set1.issuperset(set2))

