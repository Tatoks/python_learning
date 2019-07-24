def is_even(number):
    if number % 2 == 0:
        return True
    return False


for i in range(10):
    print('Is the number:', i, " a even?", is_even(i))

