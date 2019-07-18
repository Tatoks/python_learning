# if you want make a method or variable private, use _ before the name


class Jar:
    def __init__(self):
        # protected variable prefixed with _
        self._content = None

    def fill(self, content):
        self._content = content

    def empty(self):
        print('empty the jar...')
        self._content = None


myJar = Jar()
myJar.fill('sugar')

# If you try accessing _content from outside, you'll get an error
print(myJar._content)



