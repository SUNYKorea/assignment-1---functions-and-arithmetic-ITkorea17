# Name: Intae Kim   
# SBUID: 115269136
# Email: intae.kim@stonybrook.edu

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

# Simple, Just arithmetics.

def fahrenheit2celsius(fahrenheit): 
   CelsiusConversion = (5/9) * (fahrenheit - 32)
   return CelsiusConversion

# Since test does not implement printing of function values, this function can be void.
def what_to_wear(celsius):
   if celsius < -10:
       print("Wear Puffy Jacket")
   elif celsius == -10:
       print("Choose between Puffy Jacket and Scarf")
   elif -10 < celsius < 0:
       print("Wear Scarf")
   elif celsius == 0:
       print("Choose between Scarf and Sweater")
   elif 0 < celsius < 10:
       print("Wear Sweater")
   elif celsius == 10:
       print("Choose between Sweater and Light Jacket")
       
   elif 10 < celsius < 20:
       print("Wear Light Jacket")
      
   elif celsius == 20:
       print("Choose between Light Jacket and T-shirt")
       
   else:
       print("Wear T-shirt")
       

# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

# Rewriting shoelace formula. Usage of Parenthesis to be sure and clear.

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    TriangleArea = abs(((x1*y2 + x2*y3 + x3*y1) - (x1*y3 + x2*y1 + x3*y2))/2)
    return TriangleArea

# Rewriting euclidean formula.

def euclidean_distance(x1, y1, x2, y2):
    SideLength = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
    return SideLength

# Implementing euclidean formula to return parameter.

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    P1_to_P2 = euclidean_distance(x1, y1, x2, y2)
    P2_to_P3 = euclidean_distance(x2, y2, x3, y3)
    P1_to_P3 = euclidean_distance(x1, y1, x3, y3)
    TotalPerimeter = P1_to_P2 + P2_to_P3 + P1_to_P3
    return TotalPerimeter


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

# To convert degrees to radians, multiply that quantity with (pi/180)

def deg2rad(deg):
    RadianValue = deg * ((22/7)/180)
    return RadianValue

# Rewrite apothem formula. implement math import for tangent, and function deg2rad for radian conversion

def apothem(number_sides, length_side):
   import math
   ApothemValue = length_side / (2 * (math.tan(deg2rad(180/number_sides))))
   return ApothemValue

# Rewrite regular polygon area formula. Implement apothem function.

def polygon_area(number_sides, length_side):
   AreaValue = (number_sides * length_side * apothem(number_sides, length_side) / 2)
   return AreaValue


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

