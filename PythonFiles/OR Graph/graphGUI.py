from graphics import *

class GraphGUI():
    """An instance is a GUI based on an inputted Graph object.

    Instance attributes:
        graph (Graph object): a Graph containing lists of Node objects and
            Edge objects connecting those nodes."""

    def __init__(self, graph):
        self.graph = graph
        window = GraphWin(self.graph.title, 500, 400)
        for node in self.graph.nodes:
            point = Circle(Point(node.x, node.y),10)
            point.draw(window)
            text = Text(Point(node.x, node.y-20),node.name)
            text.draw(window)
        for edge in self.graph.edges:
            line = Line(Point(edge.start_node.x, edge.start_node.y),
                Point(edge.end_node.x, edge.end_node.y))
            line.draw(window)
            if edge.directed:
                line.setArrow("last")
            text = Text(line.getCenter(),str(edge.weight))
            text.draw(window)
        window.getMouse()
