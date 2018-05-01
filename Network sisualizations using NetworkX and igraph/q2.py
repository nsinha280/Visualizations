import igraph
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
import csv
from operator import itemgetter
import igraph


with open('nodelist.csv', 'r') as nodecsv: # Open the file                       
    nodereader = csv.reader(nodecsv) # Read the csv  
    nodes = [n for n in nodereader] 

with open('edgelist.csv', 'r') as edgecsv: # Open the file
    edgereader = csv.reader(edgecsv) # Read the csv     
    edges = [tuple(e) for e in edgereader]

node_names = [int(x[0]) for x in nodes]
edge_names = [(int(x[0]), int(x[1])) for x in edges]

vertices = node_names
edges = edge_names
types = [x[1] for x in nodes]
g = igraph.Graph( vertex_attrs = {"label":vertices}, edges=edges, directed=True)
g.vs["type"] = types
color_dict = {"A": "red", "B": "green", "C" : "violet"}
z=g.layout('kk')
igraph.plot(g, layout = z, vertex_color = [color_dict[type] for type in g.vs['type']], bbox = (1000, 1000))