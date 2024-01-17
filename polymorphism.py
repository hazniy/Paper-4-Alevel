#polymorphism
class shape:
    def __init__(self):
        self.__areaValue = 0
        self.__perimeterValue = 0
    def area(self):
        print("Area ", self.__areaValue)
    def perimeter(self):
        print("Perimeter ", self.__areaValue)
class rectangle(shape):
    def __init__(self, length, width):
        shape.__init__(self)
        self.__length = length
        self.__width = width
    def area (self):
        self.__areaValue = self.__length * self.__width
        print("Area ", self.__areaValue)
class circle(shape):
    def __init__(self, radius):
        shape.__init__(self)
        self.__radius = radius
    def area (self):
        self.__areaValue = self.__radius * self.__radius * 3.142
        print("Area ", self.__areaValue)
class square(shape):
    def __init__(self, length):
        shape.__init__(self)
        self.__length = length
    def area(self):
        self.__areaValue = self.__length * self.__length
        print("Area", self.__areaValue)
myCircle = circle(20)
myCircle.area()
myRectangle = rectangle (10,17)
myRectangle.area()
mySquare = square(6)
mySquare.area()
