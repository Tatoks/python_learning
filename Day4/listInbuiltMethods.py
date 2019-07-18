my_list = [2, 1, 3, 6, 5, 4]
print(my_list)
my_list.append(7)
my_list.append(8)
my_list.append("HelloWorld")
print(my_list)

my_list.remove("HelloWorld")  # sorting of mixed list throws error, so removing string

my_list.sort()  # The original object is modified
print(my_list)  # sort by default ascending

my_list.sort(reverse=True)
print(my_list)
