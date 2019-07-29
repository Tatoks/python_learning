##############################################################
# RAISE EXCEPTION
try:
    a = int(input("Enter a?"))
    b = int(input("Enter b?"))
    if b is 0:
        raise ArithmeticError;
    else:
        print("a/b = ", a / b)
except ArithmeticError:
    print("The value of b can't be 0")


##############################################################
# CUSTOM EXCEPTION DESIGN
# Custom exception class ErrorInCode designed below is a subclass of Exception
class ErrorInCode(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


try:
    a = int(input("Enter a?"))
    b = int(input("Enter b?"))

    if b is 0:
        raise ErrorInCode(2000)
except ErrorInCode as ae:
    print("Received error:", ae.data)
    ##############################################################