import math

class Node():
    """An instance is a node on a graph.

    Instance attributes:
        x: the x-coordinate of the Node
        y: the y-coordinate of the Node"""

    def __init__(self, x=0, y=0, value=1, name=None):
        self.x = x
        self.y = y
        self.value = value
        self.name = name if name != None else "Node at (" + str(self.x) + ", " + str(self.y) + ") of value " + str(self.value)
        self.neighbors = []
        self.edges = []

    def __str__(self):
        if self.name == "Node at (" + str(self.x) + ", " + str(self.y) + ") of value " + str(self.value):
            return self.name
        else:
            return str(self.name) + ": Node at (" + str(self.x) + ", " + str(self.y) + ") of value " + str(self.value)

    def distanceto(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

    def addneighbor(self, other, edge):
        self.neighbors.append(other)
        self.edges.append(edge)

    def coordinates(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
