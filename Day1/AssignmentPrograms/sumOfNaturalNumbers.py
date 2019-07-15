def sum_of_natural_numbers(number):
    total: int = 0
    while number > 0:
        total = total + number
        number -= 1
    return total


def recursive_sum(number):
    total: int = 0
    for i in range(number):
        total = total + i;
    return total


print('While Loop Sum: ', sum_of_natural_numbers(10))
print('For Loop Sum: ', sum_of_natural_numbers(10))
