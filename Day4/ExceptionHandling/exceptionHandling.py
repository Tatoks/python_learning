"""
    Python has 60+ types of exceptions.
    FileNotFoundError - File specified does not exist
    IndexError - Index out of bound
    KeyError - Key doesn't exist
    NameError - Variable name doesn't exist in local or global scope
    ValueError - Value is wrong type
"""

#    Try and except allows to exscape from crash



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
