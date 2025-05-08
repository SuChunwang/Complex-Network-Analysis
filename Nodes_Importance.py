import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def CentralityMeasures(G):
    # Betweenness
    bet = nx.betweenness_centrality(G)
    # Closeness
    clo = nx.closeness_centrality(G)
    # Eigenvector centrality
    eig = nx.eigenvector_centrality(G)
    # Degree
    deg = nx.degree_centrality(G)
    #print bet_cen, clo_cen, eig_cen
    print ("中介性:\n" + str(sorted(bet.items(),key=lambda d:d[1],reverse=True)))
    print ("接近性:\n" + str(sorted(clo.items(),key=lambda d:d[1],reverse=True)))
    print ("本征矢中心性:\n" + str(sorted(eig.items(),key=lambda d:d[1],reverse=True)))
    print ("度:\n" + str(sorted(deg.items(),key=lambda d:d[1],reverse=True)))
    
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
CentralityMeasures(G)

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='b')
node_labels = nx.get_node_attributes(G, 'desc')
nx.draw_networkx_labels(G, pos, labels=node_labels)
nx.draw_networkx_edges(G, pos,edge_color='y',width=2)
plt.show()

















