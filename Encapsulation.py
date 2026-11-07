class Myclass:

    __privateVar = 27; 

    def __privMeth(self):
        print("I'm inside class Myclass")

    def hello(self):
        print("Private variable value", Myclass.__privateVar)

foo = Myclass()
foo.hello()
foo.__privMeth