class Graph():
    """An instance is a graph containing lists of Node objects and Edge objects.

    Instance attributes:
        nodes (list): a list of Node objects.
        edges (list): a list of Edge objects connecting the nodes in the nodes
            list.
        title (string): a string that is the title of the Graph. defaults to
            "Graph"."""

    def __init__(self, nodes, edges, title="Graph"):
        self.nodes = nodes
        self.edges = edges
        self.title = title
