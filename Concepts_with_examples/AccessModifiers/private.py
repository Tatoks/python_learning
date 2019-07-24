# By default all member variables and methods are pubic
# if you want make a method or variable private, use __ before the name


class Jar:
    def __init__(self):
        self.__content = None   # private variable

    def fill(self, content):
        self.__content = content

    def empty(self):
        print('empty the jar...')
        self.__content = None


myJar = Jar()
myJar.fill('sugar')

# If you try accessing __content from outside, you'll get an error
# print(myJar.__content)
