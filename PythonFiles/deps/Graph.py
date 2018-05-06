from random import *
from .Node import Node
from .Edge import Edge
from sys import maxsize as MAX_INT
from math import floor


class Graph:

    MAX_NODES = 40
    MIN_NODES = 10
    COORD_BOUNDS = 200

    def __init__(self, seed):
        self.seed = seed
        self.nodes = []
        self.edges = []

    def removeEdge(self, e):
        e.start.neighbors.remove(e.end)
        e.end.neighbors.remove(e.start)
        e.start.edges.remove(e)
        e.end.edges.remove(e)
        self.edges.remove(e)

    def findSpanningTree(self, r):
        tree = []
        treeNodes = []

        r.shuffle(self.edges)

        for e in self.edges:
            if len(tree) == len(self.nodes) - 1:
                return tree
            if treeNodes.count(e.start) == 0 or treeNodes.count(e.end) == 0:
                if treeNodes.count(e.start) == 0:
                    treeNodes.append(e.start)
                if treeNodes.count(e.end) == 0:
                    treeNodes.append(e.end)
                tree.append(e)
        return tree


def graphBuilder(seed=0, density=-1):
    r = Random()
    randSeed = r.randint(0, MAX_INT)
    if seed == 0:
        seed = randSeed
    r.seed(seed)
    g = Graph(seed)
    numNodes = r.randint(Graph.MIN_NODES, Graph.MAX_NODES)

    for i in range(numNodes):
        nodeX = r.randint(-1 * Graph.COORD_BOUNDS, Graph.COORD_BOUNDS)
        nodeY = r.randint(-1 * Graph.COORD_BOUNDS, Graph.COORD_BOUNDS)
        n = Node(nodeX, nodeY, 1, str(i))
        g.nodes.append(n)
        for node in g.nodes:
            g.edges.append(Edge(n, node))

    randDensity = r.random()
    if density == -1:
        density = randDensity

    tree = g.findSpanningTree(r)

    toRemove = sample(g.edges, floor(len(g.edges) * (1 - density)))
    for e in toRemove:
        if tree.count(e) == 0:
            g.removeEdge(e)
    # for i in range(floor(len(g.edges)*(1-density))):
    #     e = r.choice(g.edges)
    #     if tree.count(e) == 0:
    #         g.removeEdge(e)
    return g
