import math

class Node():
    """An instance is a node on a graph.

    Instance attributes:
        x: the x-coordinate of the Node
        y: the y-coordinate of the Node"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Node at (" + str(self.x) + ", " + str(self.y) + ")"

    def distanceto(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
