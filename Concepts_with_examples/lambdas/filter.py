# Filter out all elements of a sequence

mylist = [1, 3, 4]
mylist = list(filter(lambda x: (x > 2), mylist))
print(mylist)
