import math
 
radius = float(input("Enter the radius of the circle: "))
 
# Calculate the area of the circle
area = math.pi * radius ** 2
 
# Calculate the perimeter of the circle
perimeter = 2 * math.pi * radius
 
print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter)