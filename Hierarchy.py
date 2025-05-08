import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch

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
Neighbors=[]
for k in range(len(nodes)):
    Neig=list(G.neighbors(nodes[k]))
    Neig.append(nodes[k])
    Neighbors.append(Neig)
print(Neighbors)
Similarity = np.zeros((len(A),len(A)))
for i in range(len(A)):
    for j in range(len(A)):
        Similarity[i,j] = len(list(set(Neighbors[i]).intersection(set(Neighbors[j]))))/len(list(set(Neighbors[i]).union(set(Neighbors[j]))))
Z=sch.linkage(Similarity,method='average')
fig = plt.figure()
P = sch.dendrogram(Z, labels=nodes)
plt.show()




















