import math
""""
When circle_test.py is run, it produces the following output (although the calculated area and circumference might be slightly different, depending on your computer):

$ python3 circle_test.py 
The area of the circle is 78.53981633974483
The circumference of the circle is 31.41592653589793
As a reminder, a circle with radius r has area πr2 and circumference 2πr. The value of π is stored in the constant math.pi, which you can access by importing the math module.
"""
class Circle:
  def __init__(self, radius):       # constructor
    self.radius = radius #we have to pass the radius from variable "circle"/ "circle2"
  def get_area(self):               # calculates area
    area = math.pi*(self.radius)**2    
    return area
  def get_circumference(self):      # calculates circumference
    circumference = 2*math.pi*self.radius  
    return circumference
