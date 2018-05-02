import math

class Edge():
    """An instance is an edge between two Node objects.

    Instance attributes:
        start_node (Node object): Node where the edge starts.
        end_node (Node object): Node where the edge ends.
        weight (float): numerical value associated the edge. If True, the value
            is equal to the euclidian distance between the two nodes. Otherwise
            it is equal to the given value.
        directedness: bool, true if the edge is part of an undirected graph and
            therefore has no specified direction, false if the edge is part of
            a directed graph which constitutes that the edge starts at the start
            node and ends at the end node."""

    def __init__(self, start, end, weight):
        self.start_node = start
        self.end_node = end
        self.weight = math.sqrt((self.start_node.x-self.end_node.x)**2 + (self.start_node.y-self.end_node.y)**2) if weight == True else weight
        # self.directedness = direct

    def __str__(self):
        n1 = self.start_node
        n2 = self.end_node
        return "edge from " + str(n1) + " to " + str(n2) + " of weight " + str(self.weight)
