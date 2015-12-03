__author__ = 'humberto'

import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_node("n1")
G.add_nodes_from([1,2,3,4])
G.add_edges_from([(1,2),(1,3),(2,4)])
G.add_node("n2")
G.add_node("n3")
G.add_edge("n1", "n2")
G.add_edge("n1", "n3")
G.add_edge("n2", "n3")

print(G.nodes())
print(G.edges())

print(G.has_edge("n2", "n3"))
print(G.has_edge("n1", "n3"))

print(range(1,10))

nx.draw(G, pos=nx.spring_layout(G))
plt.show()
