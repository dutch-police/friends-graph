import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G = nx.read_yaml('friends_graph.yaml')# Insert graph here
f = open('Graph.txt', 'w')

f.write(G.nodes)
f.close()
#print(G)

'''
C=nx.all_pairs_dijkstra_path(G)
'''
#sp = nx.all_pairs_shortest_path(G)
#f = open('all_pairs_dijk.txt', 'w')
#f.write(sp)
#f.close()
        
'''
# Betweenness centrality
C = nx.betweenness_centrality(G,k=10)
#print(C)
f = open('betweenness_centrality.txt', 'w')
f.write(str(C))
f.close()
'''
        
'''
# Visualize
nx.draw(G, node_color = list(C.values()), cmap = plt.cm.Blues)
plt.show()
'''
