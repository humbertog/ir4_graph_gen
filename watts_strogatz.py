__author__ = 'humberto'
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random
import numpy as np

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
# print(len(GG.edges

avg_clustering = []
avg_sp = []
# probs to be used to generate WS graphs
probs = [0.0001, 0.00035, 0.00070, 0.001, 0.0035, 0.0070, 0.01, 0.035, 0.07, 0.1, 0.3, 0.6, 1]
p0c = nx.average_clustering(nx.watts_strogatz_graph(nodes, 4, 0))
p0sp = nx.average_shortest_path_length(nx.watts_strogatz_graph(nodes, 4, 0))

# Generating the graphs and obtaining the average clustering coeff and shortest paths.
for p in probs:
    #G = genGraph_WS(nodes, p)
    G=nx.watts_strogatz_graph(nodes, 4, p)
    avg_sp.append(nx.average_shortest_path_length(G) / p0sp)
    avg_clustering.append(nx.average_clustering(G) / p0c)

print(avg_clustering)
print(avg_sp)

# Trick to plot the axis in logscale
probs_axis = []
for p in probs:
    probs_axis = probs_axis + [p*1000]

# nx.draw(GG, pos=nx.circular_layout(GG))

fig = plt.figure(figsize=(12,8))

ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_xlabel('prob * 1000')


plt.scatter(probs_axis, avg_clustering, c="b", label="Avg Clust Coeff")
plt.scatter(probs_axis, avg_sp, marker='s', c="r", label="Avg. shortest path")
plt.legend()
plt.gca().set_xscale('log')
plt.grid(True)
plt.show()


