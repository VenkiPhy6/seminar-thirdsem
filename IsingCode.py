import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
p = .04
g = nx.erdos_renyi_graph(100,p)
pos = nx.kamada_kawai_layout(g)
h = nx.Graph()
h.add_nodes_from(g.nodes())
plt.subplot(1,2, 1)
plt.title(f"Number of nodes = {len(g.nodes())}")
nx.draw(h , pos=pos)
plt.subplot(1,2, 2)
plt.title(f"Number of edges = {len(g.edges())}")
nx.draw(g, pos=pos)
plt.show()