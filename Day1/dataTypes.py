# Everything is an object in python

i = 5
j = 6.5
greeting = "Hello World"
myflag = True

print(i, j, greeting, myflag)

print('-------------Continue-------------')
# Pring Data type of the variables
print(type(i))
print(type(j))
print(type(greeting))
print(type(myflag))
print('-------------Continue-------------')
# Print address of the variables
print(id(i))
print(id(j))
print(id(greeting))
print(id(myflag))
print('-------------Continue-------------')

# Analyze address locations for immutable data types
k = 10
l = 10
m = 10.5
n = 10.5
print(id(k))  # Prints same address for both integers
print(id(l))
print(id(m))  # Prints same address for both floats
print(id(n))
l = 15  # Change value to see address change
n = 11.9
print(id(k))
print(id(l))
print(id(m))
print(id(n))
print('-------------Continue-------------')
