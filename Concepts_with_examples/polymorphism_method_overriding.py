class Animal:
    def whoAmI(self):
        print("I am Animal")

    def eat(self):
        print("Animal is eating")

    @staticmethod
    def walk():
        print('Animal is walking')


class Dog(Animal):
    def __init__(self):
        print("Dog created")

    # Method overriding
    def whoAmI(self):
        print("I am Dog")

    # dog extending base class functionality
    def bark(self):
        print("Bow Bow!!")


class Cat(Animal):
    def __init__(self):
        print("Cat Created")

    # Method overriding
    def whoAmI(self):
        print("I am Cat")

    # cat extending base class functionality
    def bark(self):
        print("Meow Meow!!")
    # End of class Cat


# polymorphism is dynamic binding technique
def func(obj):
    obj.walk()
    obj.eat()


print('-------------------------------------')
a = Animal()
d = Dog()
c = Cat()
print('-------------------------------------')
a.whoAmI()
d.whoAmI()
c.whoAmI()
print('-------------------------------------')
a.eat()
d.eat()
c.eat()
print('-------------------------------------')
a.walk()
d.walk()
c.walk()
print('-------------------------------------')
func(a)
func(d)
func(c)
