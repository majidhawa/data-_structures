import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()


G.add_edge('A', 'G')
G.add_edge('B', 'F')


G.add_node('D')
G.add_node('E')
G.add_node('F')
G.add_node('G')


G.add_edge('D', 'G')
G.add_edge('D', 'A')

G.add_edge('E', 'C')
G.add_edge('E', 'A')

G.add_edge('D', 'C') 
G.add_edge('B', 'G') 

G.add_edge('F', 'E')

nx.draw(G, with_labels=True)

plt.savefig("graph.png")


