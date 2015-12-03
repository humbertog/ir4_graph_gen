__author__ = 'humberto'
import networkx as nx
import matplotlib.pyplot as plt
import random

def genGraph_WS(n, prob):
    G=nx.Graph()
    G.add_nodes_from(range(0,n))
    # Creates
    for i in range(0,n):
        G.add_edges_from([(i, (i+1)%n), (i, (i+2)%n), (i, (i+n-2)%n), (i, (i+n-1)%n)])
    # Re-link
    for e in G.edges():
        if random.random() <= prob:
            G.add_edge(e[0], random.randrange(0, n))
            G.remove_edge(e[0], e[1])
    return G

#GG = genGraph_WS(20, .2)
#nx.draw(GG, pos=nx.circular_layout(GG))
#plt.show()

