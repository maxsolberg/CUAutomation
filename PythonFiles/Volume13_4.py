# Volume via cross-products and determinants
# Created by Max Solberg

A= float(input("X-component of vector u: "))
B= float(input("Y-component of vector u: "))
C= float(input("Z-component of vector u: "))
D= float(input("X-component of vector v: "))
E= float(input("Y-component of vector v: "))
F= float(input("Z-component of vector v: "))
G= float(input("X-component of vector w: "))
H= float(input("Y-component of vector w: "))
I= float(input("Z-component of vector w: "))
J= (A*(E*I-F*H)+B*(F*G-D*I)+C*(D*H-E*G))

Volume= (str(J))

Answer= "The volume is " + Volume

print(Answer)
