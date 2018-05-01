import igraph
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
import csv
from operator import itemgetter
import igraph

df = pd.DataFrame({'E': ['A', 'B', 'C' ],
                   'C': ['D', 'A', 'E'],
                   'A': ['E', 'F', 'G'],
                   'B': ['E', 'F', 'G'],})


# Build your graph
G = nx.from_dict_of_lists(df)
pos = nx.spring_layout(G)
# Plot it
nx.draw_networkx_nodes(G,pos,
                       nodelist=["A","B", "C", "D"],
                       node_color='g',
                       node_size=500,
                   alpha=0.8)
nx.draw_networkx_nodes(G,pos,
                       nodelist=["E","F","G"],
                       node_color='b',
                       node_size=500,
                   alpha=0.8)
nx.draw(G,pos, with_labels=True)

plt.show()