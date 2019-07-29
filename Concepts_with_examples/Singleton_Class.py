# In object-oriented programming, a singleton class is a class that can have only one object (an instance of the #class) at a time.  After first time, if we try to instantiate the Singleton class, the class should raise an #exception or the new variable should also point to the first instance created.

class Singleton:
    __single_instance = None

    def __init__(self):
        if (Singleton.__single_instance == None):
            print("creating singleton instance..\n")
            Singleton.__single_instance = self;
        else:
            raise Exception("This class is a singleton! more than one instance cannot be created for singleton class..")


# creating singleton instance the very first time
s = Singleton()

# an exception will be thrown when you try to create more than once instance for an Singleton class
s1 = Singleton()