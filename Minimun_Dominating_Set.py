import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

A = [[0,1,1,0,1,1,1,1,0,1,0],
     [1,0,0,0,1,1,1,1,0,1,0],
     [1,0,0,0,1,1,1,1,0,1,0],
     [0,0,0,0,1,0,1,1,0,1,0],
     [1,1,1,1,0,1,1,1,0,1,0],
     [1,1,1,0,1,0,0,0,0,1,0],
     [1,1,1,1,1,0,0,1,0,0,0],
     [1,1,1,1,1,0,1,0,0,1,0],
     [0,0,0,0,0,0,0,0,0,1,1],
     [1,1,1,1,1,1,0,1,1,0,1],
     [0,0,0,0,0,0,0,0,1,1,0]] # An example for test
A = np.array(A)
nodes = ['A','B','C','D','E','F','G','H','I','J','K']
G = nx.Graph()
for k in range(len(nodes)):
    node_label=nodes[k]
    G.add_node(node_label, desc=node_label)
for i in range(len(A)):
    for j in range(len(A)):
        if A[i][j]>0:
           G.add_edge(nodes[i],nodes[j])
deg = nx.degree_centrality(G)
degrank = sorted(deg.items(),key=lambda d:d[1],reverse=True)
Neighbors=[]
Degree = []
for k in range(len(nodes)):
    Neig=list(G.neighbors(nodes[k]))
    Neighbors.append(Neig)
    Degree.append(list(degrank[k])[0])
ALL = set(G.nodes())
MDS = set()
for k in range(len(nodes)):
    if len(Neighbors[k])==0:
       MDS.add(nodes[k])
REST = set()
index=0
while True:
    maxd_node = Degree[index]
    MDS.add(maxd_node)
    REST = REST.union(set(G.neighbors(maxd_node)))
    index+=1
    if MDS.union(REST) == ALL:
        break
print(MDS)
color1 = 'r'
color2 = 'b'
nodes_col = []
for k in range(len(nodes)):
    if nodes[k] in MDS:
        nodes_col.append(color1)
    else:
        nodes_col.append(color2)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color=nodes_col)
node_labels = nx.get_node_attributes(G, 'desc')
nx.draw_networkx_labels(G, pos, labels=node_labels)
nx.draw_networkx_edges(G, pos,edge_color='y',width=2)
plt.show()

















