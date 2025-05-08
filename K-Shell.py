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
Edges = list(G.edges())
importance_dict = {}
ks = 1
while G.nodes():
    temp = []
    node_degrees_dict = dict(G.degree())
    kks = min(node_degrees_dict.values())
    while True:
        for k, v in node_degrees_dict.items():
            if v == kks:
                temp.append(k)
                G.remove_node(k)
        node_degrees_dict = dict(G.degree())
        if kks not in node_degrees_dict.values():
            break
    importance_dict[ks] = temp
    ks += 1
S = sorted(importance_dict.items(),reverse=True)
nodes = []
coordinates = []
nodes_col = []
colors = []
for i in range(len(S)):
    color=((len(S)-i)/len(S),0,i/len(S))
    colors.append(color)
theta = np.arange(0,2*np.pi,0.01)
for i in range(len(S)):
    R = i+1
    x=R*np.cos(theta)
    y=R*np.sin(theta)
    plt.plot(x,y,c=colors[i])
    shell = S[i][1]
    n = len(shell)
    col = colors[i]
    for j in range(n):
        nodes.append(shell[j])
        coordinates.append([R*np.cos((j+1.3*i+1)*2*np.pi/n),R*np.sin((j+1.3*i+1)*2*np.pi/n)])
        nodes_col.append(col)
vnode = np.array(coordinates)
npos = dict(zip(nodes,vnode))
pos = {}
pos.update(npos)
nlabels = dict(zip(nodes,nodes))
G = nx.Graph()
for k in range(len(nodes)):
    node_label=nodes[k]
    G.add_node(node_label, desc=node_label)
for i in range(len(nodes)):
    for j in range(i):
        if ((nodes[i],nodes[j])in Edges) or ((nodes[j],nodes[i])in Edges):
           G.add_edge(nodes[i],nodes[j])
nx.draw_networkx_nodes(G, pos, node_color=nodes_col)
node_labels = nx.get_node_attributes(G, 'desc')
nx.draw_networkx_labels(G, pos, labels=node_labels)
nx.draw_networkx_edges(G, pos,edge_color='y',width=1)
plt.xlim(-(len(S)+1),(len(S)+1))
plt.ylim(-(len(S)+1),(len(S)+1))
plt.show()















