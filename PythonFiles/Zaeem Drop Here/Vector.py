# Vector class
# Written by Zaeem Rana

class Vector(object):

    """
    Creates a new Vector with x,y,z

    x,y,z are defaulted to 0

    Parameter x: x for x postion
    Precondition: x is a number

    Parameter y: y for z postion
    Precondition: y is a number

    Parameter z: z for z postion
    Precondition: z is a number
    """
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    """
    Just Getters for the components
    """
    def getX():
        return self._x
    def getY():
        return self._y
    def getZ():
        return self._z

    """
    Just setters for the components.
    Precondition: x,y,z are numbers
    """
    def setX(self, x):
        self._x = x
    def setY(self, y):
        self._y = y
    def setZ(self, z):
        self._z = z

    """
    Return the magnitude of the vector
    """
    def magnitude():
        return (x**2 + y**2 + z**2)**0.5

    """
    Return the dot Product of this Vector and Vector v

    Parameter: v is a Vector to conduct a dot product with
    Parameter: v is a Vector class
    """
    def dotProduct(self, v):
        return self.getX() * v.getX() + self.getY() * v.getY() + self.getZ() * v.getZ()

    """
    Return the cross Product of this Vector and Vector v

    Parameter: v is a Vector to conduct a cross product with
    Parameter: v is a Vector class
    """
    def crossProduct(self, v):
        newX = self.getY() * v.getZ() - self.getZ() * v.getY()
        newY = self.getX() * v.getZ() - self.getZ() * v.getX()
        newZ = self.getX() * v.getY() - self.getY() * v.getX()

        return Vector(newX, newY, newZ)
