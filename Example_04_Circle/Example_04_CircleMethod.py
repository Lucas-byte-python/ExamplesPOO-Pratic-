# Method of Class--------------------------------------
# Used to Manipulate Class Attributes------------------

class Circle2:
    __full_circle = 0 # Attribute Private

    def __init__(self, pointX, pointY, ray):
        self.pointX = pointX
        self.pointY = pointY
        self.ray = ray
        type(self).__full_circle += 1 # Add 1

    # @classmethod Create the Method of Class
    @classmethod
    def get_full_circle(cls):
        return cls.__full_circle