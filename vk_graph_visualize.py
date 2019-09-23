import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G = nx.balanced_tree(3, 3) # Insert graph here

# Betweenness centrality
C = nx.betweenness_centrality(G)

# Visualize
nx.draw(G, node_color = list(C.values()), cmap = plt.cm.Blues)
plt.show()