# Class is a collection of objects
# Class is a blueprint for creating an object
# Class is a logical Entity

# An Object is an instance of class


class Calculator:
    def add(self, i, j):
        # self - (this) pointer pointing to current instance which is invoking
        # Any method called via object instance should use self
        self.i = i  # Instance variable
        self.j = j  # Instance variable
        return i + j
        # End of method add
    # End of class Calculator


calc = Calculator()
print(calc.add(1, 2))
print(calc.i, calc.j)
print(type(calc))  # <class '__main__.Calculator'>

# Type of a class instance is __main__.Calculator, this is beacuse we are running in standalone mode
# Python assigns the start of app as __main__ module
