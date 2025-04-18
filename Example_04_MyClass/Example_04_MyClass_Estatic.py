# Method Static------------------------------------------
class MyClass:
    @staticmethod # Method Static
    def method_static(x, y):
        return x + y

result = MyClass.method_static(3, 5)
print(result)
# Exit? 8

# You don't Need to Create an Instance of the Class to use the Static Method.

obj = MyClass()
result = obj.method_static(10, 20)
print(result)
# Exit? 30