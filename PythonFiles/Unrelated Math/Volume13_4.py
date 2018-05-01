# Volume via cross-products and determinants
# Created by Max Solberg

a= float(input("X-component of vector u: "))
b= float(input("Y-component of vector u: "))
c= float(input("Z-component of vector u: "))
d= float(input("X-component of vector v: "))
e= float(input("Y-component of vector v: "))
f= float(input("Z-component of vector v: "))
g= float(input("X-component of vector w: "))
h= float(input("Y-component of vector w: "))
i= float(input("Z-component of vector w: "))
j= (a*(e*i-f*h)+b*(f*g-d*i)+c*(d*h-e*g))

Volume= (str(j))

Answer= "The volume is " + Volume

print(Answer)
