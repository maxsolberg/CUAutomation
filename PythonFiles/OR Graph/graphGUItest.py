import edge as e
import node as n
import graph as g
import graphGUI
node1 = n.Node(100,200,1,"1")
node2 = n.Node(200,125,1,"2")
node3 = n.Node(200,275,1,"3")
node4 = n.Node(300,125,1,"4")
node5 = n.Node(300,275,1,"5")
node6 = n.Node(400,200,1,"6")
nodelist = [node1,node2,node3,node4,node5,node6]
edge12 = e.Edge(node1,node2,None,True)
edge13 = e.Edge(node1,node3,None,True)
edge24 = e.Edge(node2,node4,None,True)
edge35 = e.Edge(node3,node5,None,True)
edge46 = e.Edge(node4,node6,None,True)
edge56 = e.Edge(node5,node6,None,True)
edgelist = [edge12,edge13,edge24,edge35,edge46,edge56]
graph1 = g.Graph(nodelist,edgelist)
graphgui = graphGUI.GraphGUI(graph1,500,400)
