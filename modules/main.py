from math_operations import calculator, geometry

result = calculator.add(5, 3)
print("The addition result is:", result)

result = calculator.subtract(10, 4)
print("The subtraction result is:", result)

rect_area = geometry.rectangle_area(5, 3)
print("The rectangle area is:", rect_area)

tri_area = geometry.triangle_area(4, 2)
print("The triangle area is:", tri_area)

circ_area = geometry.circle_area(3)
print("The circle area is:", circ_area)
