# By default all member variables and methods are pubic by default in python


class Jar:
    def __init__(self):
        self.content = None

    def fill(self, content):
        self.content = content

    def empty(self):
        print('empth the jar...')
        self.content = None


myJar = Jar()
myJar.content = 'sugar'
print(myJar.content)
