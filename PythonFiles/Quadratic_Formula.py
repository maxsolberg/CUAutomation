# Quadratic Formula
# Created by Max Solberg

import math

print("Input A, B, and C for Ax^2+Bx+C=0")
A= int(input("A: "))
B= int(input("B: "))
C= int(input("C: "))
D= (-B+math.sqrt(B**2-4*A*C))/(2*A)
E= (-B-math.sqrt(B**2-4*A*C))/(2*A)
print("The solutions to the equation " + str(A) + "x^2+" + str(B) + "x+" + str(C) + " are: " + str(D) + " and " + str(E))
