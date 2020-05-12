from AllShapes import *


circle = Circle(0, 0)
circle.area = Circle.area(circle, 7)  # area variable is public and can be accessed outside the class
print("Area of circle : " + str(circle.area))
circle.perimeter = Circle.perimeter(circle, 7)  # perimeter variable is public and can be accessed outside the class
print("Perimeter of circle : " + str(circle.perimeter))

triangle = Triangle(0, 0)
triangle.area = Triangle.area(triangle, 10, 5)  # area variable is public and can be accessed outside the class
print("Area of triangle : " + str(triangle.area))

square = Square(0, 0)
square.area = Square.area(square, 10)  # area variable is public and can be accessed outside the class
print("Area of square : " + str(square.area))
square.perimeter = Square.perimeter(square, 10)  # perimeter variable is public and can be accessed outside the class
print("Perimeter of square : " + str(square.perimeter))

rectangle = Rectangle(0, 0)
rectangle.area = Rectangle.area(rectangle, 10, 5)  # area variable is public and can be accessed outside the class
print("Area of rectangle : " + str(rectangle.area))
rectangle.perimeter = Rectangle.perimeter(rectangle, 10, 5)  # perimeter variable is public and can be accessed outside the class
print("Perimeter of rectangle : " + str(rectangle.perimeter))

parallelogram = Parallelogram(0, 0)
parallelogram.area = Parallelogram.area(parallelogram, 9, 6)  # area variable is public and can be accessed outside the class
print("Area of parallelogram : " + str(parallelogram.area))

trapezium = Trapezium(0, 0)
trapezium.area = Trapezium.area(trapezium, 5, 10, 5)  # area variable is public and can be accessed outside the class
print("Area of trapezium : " + str(trapezium.area))

rhombus = Rhombus(0, 0)
rhombus.area = Rhombus.area(rhombus, 10, 5)  # area variable is public and can be accessed outside the class
print("Area of rhombus : " + str(rhombus.area))
rhombus.perimeter = Rhombus.perimeter(rhombus, 10)  # perimeter variable is public and can be accessed outside the class
print("Perimeter of rhombus : " + str(rhombus.perimeter))

pentagon = Pentagon(0, 0)
pentagon.perimeter = Pentagon.perimeter(pentagon, 10)  # perimeter variable is public and can be accessed outside the class
print("Perimeter of pentagon : " + str(pentagon.perimeter))

hexagon = Hexagon(0, 0)
hexagon.perimeter = Hexagon.perimeter(hexagon, 10)  # perimeter variable is public and can be accessed outside the class
print("Perimeter of hexagon : " + str(hexagon.perimeter))

heptagon = Heptagon(0, 0)
heptagon.perimeter = Heptagon.perimeter(heptagon, 10)  # perimeter variable is public and can be accessed outside the class
print("Perimeter of heptagon : " + str(heptagon.perimeter))
