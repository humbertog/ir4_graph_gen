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
    edges = G.edges()
    to_add = []
    to_rm = []
    while len(edges) > 0:
        e = edges.pop()
        if random.random() <= prob:
            # Avoid duplicated and self links
            seen = [k[1] for k in to_add if k[0] == e[0]]
            seen = seen +  [k[0] for k in to_add if k[1] == e[0]]
            possible_new = set(range(0, n)) - set(G[e[0]].keys()) - set(seen)
            possible_new = possible_new - set([e[0]])
            # Adding and removing lists
            to_add.append((e[0], random.choice(list(possible_new))))
            to_rm.append((e[0], e[1]))

    G.remove_edges_from(to_rm)
    G.add_edges_from(to_add)

    return G

# GG = genGraph_WS(20, 0)
# print(len(GG.edges()))

# GG = genGraph_WS(20, .5)
# print(len(GG.edges()))


# nx.draw(GG, pos=nx.circular_layout(GG))
# plt.show()

