from graphics import *

class GraphGUI:
    """An instance is a GUI based on an inputted Graph object.

    Instance attributes:
        graph (Graph object): a Graph containing lists of Node objects and
            Edge objects connecting those nodes.
        width (int): width of the GraphGUI object.
        height (int): height of the GraphGUI object."""

    def __init__(self, graph,width=800,height=800):
        self.graph = graph
        self.nodes = dict()
        self.edges = dict()

        for edge in self.graph.edges:
            line = Line(Point(edge.start.x, edge.start.y),
                Point(edge.end.x, edge.end.y))
            if edge.directed:
                line.setArrow("last")
            self.edges[edge] = line
            # text = Text(line.getCenter(),str(edge.weight))
            # text.draw(win)

        for node in self.graph.nodes:
            point = Circle(Point(node.x, node.y),10)
            point.setFill("black")
            self.nodes[node] = point

        win = GraphWin("Window", width, height)
        win.setCoords(-1*self.graph.COORD_BOUNDS - 20, -1*self.graph.COORD_BOUNDS - 20, self.graph.COORD_BOUNDS + 20, self.graph.COORD_BOUNDS + 20)

        info = Text(Point(0, self.graph.COORD_BOUNDS + 10), "Seed: " + str(self.graph.seed))
        info.draw(win)

        for line in list(self.edges.values()):
            line.draw(win)
        win.getMouse()
        for node in list(self.nodes.keys()):
            self.nodes[node].draw(win)
            text = Text(Point(node.x, node.y),node.name)
            text.setTextColor("white")
            text.draw(win)
