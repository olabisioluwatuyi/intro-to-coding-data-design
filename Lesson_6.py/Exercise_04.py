# Area Calculator: Define functions for calculating the area of a circle, square,
# and triangle. Prompt the user to choose a shape and input the necessary parameters 
# to calculate and display the area.
# The area of a circle is calculated as follows: area = pi * radius * radius
# The area of a square is calculated as follows: area = length * length
# The area of a triangle is calculated as follows: area = 0.5 * base * height


def calculate_area_circle_formula(radius):
    return 3.14 * radius * radius

# This function calculates the circle area
def calculate_area_circle():
  radius = float(input("What's the circle radius?"))
  area = calculate_area_circle_formula(radius)
  return area

def calculate_area_square():
  length = float(input("What's the length of the square side?"))
  area = length * length
  return area

def calculate_area_triangle():
  base = float(input("What's the triangle base?"))
  height = float(input("What's the triangle height?"))
  area = 0.5 * base * height
  return area

def calculate_area(shape):
  if (shape == "circle"):
    return calculate_area_circle()
  elif (shape == "square"):
    return calculate_area_square()
  elif (shape == "triangle"):
    return calculate_area_triangle()
  else: 
    print("I need a proper shape!")
    return None

shape_choice = input("Which shape are you calculating the area for? (circle/square/triangle)")
print(calculate_area(shape_choice))