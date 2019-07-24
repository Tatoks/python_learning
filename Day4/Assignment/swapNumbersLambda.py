from copy import copy


swapper = lambda l, m: (m, l)

x = 10
y = 11
print(x, y)


x, y = swapper(x, y)


print(x, y)
