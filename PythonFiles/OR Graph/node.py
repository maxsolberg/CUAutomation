import math

class Node():
    """An instance is a node on a graph.

    Instance attributes:
        x (float): the x-coordinate of the Node
        y (float): the y-coordinate of the Node
        value (float): the value associated with a given Node object. This could
            represent the population of a city Node, the value of a gem Node,
            etc.
        name (str): the name associated with a given Node object.
        neighbors (list): a list of a given Node object's neighboring nodes.
            these are nodes that are reachable from the given Node by edges
            connecting the two.
        edges (list): a list of edges leaving the Node. This includes
            non-directed edges and directed edges with this Node as the
            endpoint."""

    def __init__(self, x=0, y=0, value=1, name=None):
        self.x = x
        self.y = y
        self.value = value
        self.name = name if name != None else self.coordinates() # "Node at (" + str(self.x) + ", " + str(self.y) + ") of value " + str(self.value)
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
