class Edge():
    """An instance is an edge between two Node objects.

    Instance attributes:
        start_node (Node object): Node where the edge starts.
        end_node (Node object): Node where the edge ends.
        weight (float): numerical value associated the edge. If True, the value
            is equal to the euclidian distance between the two nodes. Otherwise
            it is equal to the given value.
        directed: bool, false if the edge is part of an undirected graph and
            therefore has no specified direction, true if the edge is part of
            a directed graph which constitutes that the edge starts at the start
            node and ends at the end node."""

    def __init__(self, start, end, weight=None, directed=False):
        self.start_node = start
        self.end_node = end
        self.weight = self.start_node.distanceto(self.end_node) if weight == None else weight
        self.directed = directed
        self.start_node.addneighbor(self.end_node, self)
        if directed == False:
            self.end_node.addneighbor(self.start_node, self)

    def __str__(self):
        n1 = self.start_node
        n2 = self.end_node
        if self.directed == True:
            return "edge of weight " + str(self.weight) + " connecting " + str(n1) + " to " + str(n2)
        else:
            return "edge of weight " + str(self.weight) + " connecting " + str(n1) + " and " + str(n2)
