# My Class----Method Private-(_)-or-(__)-----------------------------------
class MyClass:
    def __init__(self):
        self._attribute_private = 42

    def _method_private1(self):
        print("Method Private!")

    def method_public1(self):
        print("Method Public One!")
        self._method_private1()

    def __method_private2(self):
        print("Method Strong Private!")

    def method_public2(self):
        print("Method Public Two!")
        self.__method_private2()

obj = MyClass()
obj.method_public1() # Tell the Method Public
# Exit:
# Method Public One!
# Method Private!
print()

obj._method_private1() # It Work, Not Stonks!
# Exit:
# Method Private!
print()

obj.method_public2() # Tell the Method Public
# Exit:
# Method Public Two!
# Method Strong Private!
print()

obj._MyClass__method_private2() # It Work, Not Stonks!
# Exit:
# Method Strong Private!