class Edge:

    def __init__(self, start, end, weight=None, directed=False):
        self.start = start
        self.end = end
        self.directed = directed
        self.weight = weight if weight != None else start.distTo(end)

        start.addNeighbor(end, self)
        if self.directed == False:
            end.addNeighbor(start, self)

    def __str__(self):
        if self.directed:
            return "Edge from " + self.start.name + " to " + self.end.name + " with weight " + str(self.weight)
        return "Edge connecting " + self.start.name + " and " + self.end.name + " with weight " + str(self.weight)

    """ return the node on the other end of this edge from n"""
    def other(self, n):
        if start == n:
            return end
        return start
