add_l = lambda x, y: y / x
result = add_l(2, 4)
print(result)

print(add_l)
print(type(add_l))

# lambda function to determine max of two numbers
maximum = lambda x, y: x if x > y else y
# lambda function to determine min of two numbers
minimum = lambda x, y: x if x < y else y

max3 = lambda x, y, z: z if z > (x if x > y else y) else (x if x > y else y)

print(minimum(1, 2), maximum(1, 2), max3(1, 2, 3))

square = lambda x: x ** 2
print(square(3))

# To-do swap using lambda
swap = lambda x, y: y is x and x is y
l = 10
m = 11
swap(l, m)

print(l, m)
