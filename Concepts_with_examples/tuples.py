# Tuple is an ordered sequence of items same as list.The only difference is that tuples are immutable.
# Tuples once created cannot be modified. Tuples are immutable.

my_tuple = ("apples", "bananas", "oranges", "kiwis")

# accessing tuple using index
print(my_tuple[0])
print(my_tuple[3])

# slicing tuple
print(my_tuple[1:4])
print(my_tuple[-2:])
print(my_tuple[:-2])

print("--------------")
# iterating over tuple
for item in my_tuple:
    print(item)

print("--------------")
# check  if item exists
if "apples" in my_tuple:
    print("Yes")

print("--------------")

# tuple is immutable hence it will throw an error when you try to modify an element in a tuple or delete an item in a tuple
my_tuple[0] = 'ambrosia'

# tuple is immutable hence it will throw an error when you try to modify an element in a tuple or delete an item in a tuple
del my_tuple[0]

# tuple destructor
del my_tuple

my_tuple = ("apples", "bananas", "oranges", "kiwis")
print("--------------")
# reverse tuple
print(my_tuple[::-1])

print("--------------")
# sort tuple
print(sorted(my_tuple))

print("--------------")
# convert a list into tuple
my_list = ['apples', 'bananas', 'kiwis', 'oranges']
my_tuple = tuple(my_list)
print(type(my_tuple))
print(my_tuple)

print("--------------")
# concatenate tuples
my_tuple1 = ("apples", "bananas")
my_tuple2 = ("oranges", "kiwis")
print(my_tuple1 + my_tuple2)

print("--------------")
# convert tuple to an dictionary
my_tuple = (('a', "apple"), ('b', "banana"), ('c', "cat"), ('d', "dog"))

dict1 = dict(i for i in my_tuple)
print(dict1)

print("--------------")
# convert a tuple to an string
test = ("apple", "banana", "orange", "kiwi")

strtest = ','.join(test)
print(strtest)

print("--------------")
# tuple index method
test = ("apple", "banana", "orange", "kiwi")
print(test.index("orange"))