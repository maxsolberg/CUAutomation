# Area of a Cylinder
# By Jacob Johansen

import math as m

a= float(input("radius of cylinder: "))
b= float(input("height of cylinder: "))
c=2*m.pi*a*b+2*m.pi*a**2
print("area of the cylinder: " + str(c))
