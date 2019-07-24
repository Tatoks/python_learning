i = input("Enter a number       :")
j = input("Enter another number :")

try:
    if i == '0' or j == '0':
        raise ValueError("Input cannot be zero")
    print(i+j)
except ValueError as ve:
    print(ve)
except Exception as e:
    print(e)
