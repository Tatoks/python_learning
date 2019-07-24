class Jar:
    my_static_variable = 'Hello World'

    def __init__(self):
        self.content = None

    def fill(self, content):
        self.content = content

    def empty(self):
        print('Empty the jar...')
        self.content = None


myJar = Jar()
myJar.content = 'sugar'
print(Jar.my_static_variable)  # Accessed without creating object
print(myJar.my_static_variable)  # Even objects can access

myJar2 = Jar()
myJar2.my_static_variable = "changed the static value"
print(myJar2.my_static_variable)  # Even objects can access
print(Jar.my_static_variable)  # Accessed without creating object
print(myJar.my_static_variable)  # Even objects can access
