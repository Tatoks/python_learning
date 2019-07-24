# Basic python methods Example
def add(i, j):
    return i + j


def empty_method(i, j):
    pass


def return_none():
    return None


def add_return_none2(i, j):
    print('Sum=', i + j)
    return


print(add(10, 1))
print(empty_method(10, 1))
print(return_none())
print(add_return_none2(11, 2))


# parameter j is optional, if not assigned a value during method call, the it is default to 10


def add_two_numbers(i, j=10):
    return i + j;


print(add_two_numbers(1, 23))
print(add_two_numbers(1))


# FUNCTION which accepts any number of arguments
def add(*arr):
    total = 0
    for i in arr:
        total = total + i
    return total


print(add(1, 3, 4))


# RECURSIVE FUNCTION CALL Example
def factorial(i):
    if i <= 1:
        return 1
    elif i == 0:
        return 1
    else:
        return i * factorial(i - 1)


print(factorial(7))
