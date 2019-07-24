# map() function takes in lambda function and a list.

# program with map function : a new list is returned which contains all the lambda modified items
my_list = [1, 2, 3, 4, 5, 6]
my_list = list(map(lambda x: (x**2), my_list))
print(my_list)
