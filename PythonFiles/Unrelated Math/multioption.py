# Multi Options
# By Jacob Johansen

print("Option 1 is rectangle\n Option 2 is circle\n Option 3 is sphere\n Option 4 is right cylinder\n Option 5 is trapezoid\n Option 6 is triangle")
option=int(input("Option: "))

if   option==1:
    a= float(input("length of the rectangle: "))
    b= float(input("width of the rectangle: "))
    c= a*b
    print("area of the rectangle is: " + str(c))

elif option==2:
    import math as m

    a= float(input("radius of circle: "))
    b= m.pi*a**2
    print("area of the circle:" + str(b))

elif option==3:
    import math as m

    a= float(input("radius of sphere: "))
    b= 4*m.pi*a**2
    print("area of the sphere: " + str(b))

elif option==4:
    import math as m

    a= float(input("radius of cylinder: "))
    b= float(input("height of cylinder: "))
    c=2*m.pi*a*b+2*m.pi*a**2
    print("area of the cylinder: " + str(c))

elif option==5:
    a= float(input("base 1 of trapezoid: "))
    b= float(input("base 2 of trapezoid: "))
    c= float (input("height of trapezoid: "))
    d= (a+b)*0.5*c
    print("area of the trapezoid is: " + str(d))

elif option==6:
    a= float(input("base of triangle: "))
    b= float(input("width of triangle: "))
    c=0.5*a*b
    print("area of the triangle is: " + str(c))

else:
    print("no valid option chosen ")
