from Shapes import Shapes  # abstraction


class Circle(Shapes):
    __radius = 7  # private access specifier
    print("Radius within class circle : " + str(__radius))  # radius accessible within the class circle only

    def perimeter(self, radius):
        self.perimeter = 2 * 3.14 * radius
        return self.perimeter

    def area(self, radius):
        self.area = 3.14 * radius * radius
        return self.area


class Triangle(Shapes):
    __base = 10
    __height = 5
    print("Base within class triangle : " + str(__base))  # base accessible within the class triangle only
    print("Height within class triangle : " + str(__height))  # height accessible within the class triangle only

    def area(self, base, height):
        self.area = 0.5 * base * height
        return self.area


class Square(Shapes):
    __length = 10
    print("Length within class square : " + str(__length))  # length accessible within the class square only

    def perimeter(self, length):
        self.perimeter = 4 * length
        return self.perimeter

    def area(self, length):
        self.area = length * length
        return self.area


class Rectangle(Shapes):
    __length = 10
    __breadth = 5
    print("Length within class rectangle : " + str(__length))  # length accessible within the class rectangle only
    print("Breadth within class rectangle : " + str(__breadth))  # breadth accessible within the class rectangle only

    def perimeter(self, length, breadth):
        self.perimeter = 2 * (length + breadth)
        return self.perimeter

    def area(self, length, breadth):
        self.area = length * breadth
        return self.area


class Parallelogram(Shapes):
    __base = 9
    __height = 6
    print("Base within class parallelogram : " + str(__base))  # base accessible within the class parallelogram only
    print("Height within class parallelogram : " + str(__height))  # height accessible within the class parallelogram only

    def area(self, base, height):
        self.area = base * height
        return self.area


class Trapezium(Shapes):
    __smallerside = 5
    __longerside = 10
    __height = 5
    print("Height within class trapezium : " + str(__height))  # height accessible within the class trapezium only
    print("Smaller side within class trapezium : " + str(__smallerside))  # smallerside accessible within the class trapezium only
    print("Longer side within class trapezium : " + str(__longerside))  # longerside accessible within the class trapezium only

    def area(self, smallerside, longerside, height):
        self.area = (height / 2) * (smallerside + longerside)
        return self.area


class Rhombus(Shapes):
    __length = 10
    __height = 5
    print("Length within class rhombus : " + str(__length))  # length accessible within the class rhombus only
    print("Height within class rhombus : " + str(__height))  # height accessible within the class rhombus only

    def perimeter(self, length):
        self.perimeter = 4 * length
        return self.perimeter

    def area(self, length, height):
        self.area = length * height
        return self.area


class Pentagon(Shapes):
    __length = 10
    print("Length within class pentagon : " + str(__length))  # length accessible within the class pentagon only

    def perimeter(self, length):
        self.perimeter = length * 5
        return self.perimeter


class Hexagon(Shapes):
    __length = 10
    print("Length within class hexagon : " + str(__length))  # length accessible within the class hexagon only

    def perimeter(self, length):
        self.perimeter = length * 6
        return self.perimeter


class Heptagon(Shapes):
    __length = 10
    print("Length within class heptagon : " + str(__length))  # length accessible within the class heptagon only

    def perimeter(self, length):
        self.perimeter = length * 7
        return self.perimeter
