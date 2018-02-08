# Volume via cross-products and determinants

A= int(input("X-component of vector u:"))
B= int(input("Y-component of vector u:"))
C= int(input("Z-component of vector u:"))
D= int(input("X-component of vector v:"))
E= int(input("Y-component of vector v:"))
F= int(input("Z-component of vector v:"))
G= int(input("X-component of vector w:"))
H= int(input("Y-component of vector w:"))
I= int(input("Z-component of vector w:"))
J= (A*(E*I-F*H)+B*(F*G-D*I)+C*(D*H-E*G))

Volume= (str(J))

Answer= "The volume is " + Volume

print(Answer)
