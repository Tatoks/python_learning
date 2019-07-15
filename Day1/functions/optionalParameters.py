# parameter j is optional, if not assigned a value during method call, the it is default to 10


def add_two_numbers(i, j=10):
    return i + j;


print(add_two_numbers(1, 23))

print(add_two_numbers(1))
