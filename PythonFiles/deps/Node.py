import math as m


class Node:

    def __init__(self, x=0, y=0, val=1, name=None):
        self.x = x
        self.y = y
        self.val = val
        self.neighbors = []
        self.edges = []
        self.name = name if name != None else "(" + \
            str(self.x) + ", " + str(self.y) + ")"

    def __str__(self):
        return "{Node \"" + str(self.name) + "\" at (" + str(self.x) + ", " + str(self.y) + ") with value: " + str(self.val) + "}"

    def distTo(self, other):
        return m.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def addNeighbor(self, other, edge):
        self.neighbors.append(other)
        self.edges.append(edge)
