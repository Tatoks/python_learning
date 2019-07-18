num1 = 10
num2 = 0

try:
    # your program goes here
    a = num1 / num2
    print("Try Block: ", a)
except ZeroDivisionError as e:
    print("Error occurred: ", e)
    print(type(e))
except (FileNotFoundError, ValueError) as e:
    print("Handling multiple types of exceptions in single statement")
except Exception as e:
    print("General Exception:", e)
finally:
    print("Finally block")
