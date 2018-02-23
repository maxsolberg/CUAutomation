# Quadratic Formula
# Created by Max Solberg

import math

print("Input A, B, and C for Ax^2+Bx+C=0")
a= float(input("A: "))
b= float(input("B: "))
c= float(input("C: "))
d= (-b+math.sqrt(b**2-4*a*c))/(2*a)
E= (-b-math.sqrt(B**2-4*a*c))/(2*a)
print("The solutions to the equation " + str(a) + "x^2+" + str(b) + "x+" + str(c) + " are: " + str(d) + " and " + str(e))
