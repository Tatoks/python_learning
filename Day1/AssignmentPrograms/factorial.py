def factorial(number: int):
    fact: int = 1
    while number > 1:
        fact *= number
        number = number - 1
    return fact


def recursive_factorial(number: int):
    fact: int = number;
    if number <= 1:
        return 1
    else:
        fact = fact * recursive_factorial(number - 1)
    return  fact


argument = 5
print("Non Recursive Method: ", factorial(argument))
print("Recursive Method: ", recursive_factorial(argument))
