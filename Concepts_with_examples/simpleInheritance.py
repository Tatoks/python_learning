class human:
    def __init__(self, name, gender='female'):
        self.name = name
        self.gender = gender

    def greet(self, message):
        self.message = message
        print(self.message, self.name)


class man(human):
    def __init__(self, name, age, message):
        super().__init__(name, 'male')
        self.age = age
        self.greet(message)
        # self.age = input("Enter Age:")

    def printDetails(self):
        print(self.message, self.name, self.age, self.gender)


person1 = man("Abhi", 28, "Hello")
person1.printDetails()
