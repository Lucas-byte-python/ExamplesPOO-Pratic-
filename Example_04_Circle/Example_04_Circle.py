class Circle():
    full_circle = 0

    def __init__(self, pointX, pointY, ray):
        self.pointX = pointX
        self.pointY = pointY
        self.ray = ray
        Circle.full_circle += 1