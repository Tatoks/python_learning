my_greetings = "helloworld"
iter_str = iter(my_greetings)
print(next(iter_str), end="")
print(next(iter_str), end="")
print(next(iter_str), end="")
print(next(iter_str), end="")
print(next(iter_str), end="")
print(next(iter_str), end="")
print(next(iter_str), end="")
print(next(iter_str), end="")
print(next(iter_str), end="")
print(next(iter_str), end="")


# Printed complete string, next iteration will throw error
# print(next(iter_str))

print()
for i in my_greetings:
    # Internally iterator is being called on string __iter__
    print(i, end="")
    # print(my_greetings.__iter__())