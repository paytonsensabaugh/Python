# 4.1 Functions 

def square(side):
    print("Enter a side value: ")

def circle(radius):
    print("enter the radius") 

square(1)
side1 = int(input())
square(1)
side2 = int(input())
circle(1) 
radius = int(input())

result = side1 * side2
print(f"The area of the square is {result} square unit.")

pie = 3.14 
result1 = pie * radius * radius 
print(f"The area of the circle is {result1:.2f} square units.")