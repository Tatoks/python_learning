# List is an ordered sequence of items. List is mutable
# List once created can be modified.
my_list = ["apples", "bananas", "oranges", "kiwis"]

print("--------------")
print(my_list)

print("--------------")
# accessing list using index
print(my_list[0])
print(my_list[3])

# slicing list
print(my_list[1:4])
print(my_list[-2:])
print(my_list[:-2])

print("--------------")
# iterating over list
for item in my_list:
    print(item)

print("--------------")
# check  if item exists
if "apples" in my_list:
    print("Yes")

print("--------------")
# modify list element
my_list[2] = "guava"
print(my_list)

print("---------------")
# list is mutable. try delete an element from list
del my_list[2]

print("list destructor")
# delete list
del my_list

print("--------------")
my_list = ["apples", "bananas", "oranges", "kiwis"]

print("list is mutable. try append an element to an list")
my_list.append("pomegranate")
print(my_list)

print("--------------")
# reverse list
print(my_list[::-1])

print("--------------")
# sort list
print(sorted(my_list))

print("--------------")
# concatenate lists
my_list1 = ["apples", "bananas"]
my_list2 = ["oranges", "kiwis"]
print(my_list1 + my_list2)

print("--------------")
# list index method
my_list = ["apple", "banana", "orange", "kiwi"]
print(my_list.index("orange"))

print("--------------")
# convert a list into set
my_list = ['apples', 'bananas', 'kiwis', 'oranges']
my_list = set(my_list)
print(type(my_list))
print(my_list)

print("--------------")
# convert list to an dictionary
my_list = [['a', "apple"], ['b', "banana"], ['c', "cat"], ['d', "dog"]]
dict1 = dict(i for i in my_list)
print(dict1)

print("--------------")
# convert a list to an string
my_list = ["apple", "banana", "orange", "kiwi"]
strtest = ','.join(my_list)
print(strtest)

# list copy : shallow copy and deep copy methods
import copy

my_list = ["apple", "banana", "orange", "kiwi"]

print("--------------")
new_list = copy.copy(my_list)
print(my_list, id(my_list))
print(new_list, id(new_list))

print("--------------")
new_list = copy.deepcopy(my_list)
print(my_list, id(my_list))
print(new_list, id(new_list))