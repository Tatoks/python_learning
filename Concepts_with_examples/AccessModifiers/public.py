#PUBLIC : All member variables and methods are public by default in Python.


class Jar:
    def __init__(self):
        self.content = None

    def fill(self, content):
        self.content = content

    def empty(self):
        print('empty the jar...')
        self.content = None



myJar = Jar()
myJar.content = "salt"
print(myJar.content)


myJar.empty()
myJar.fill('sugar')
print(myJar.content)