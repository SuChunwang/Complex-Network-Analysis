import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def loc_net(A,nodes,node):
    
    '''
     A: Adjacency matrix of the network.
     nodes: Node list of the network.The order of the list elements is the same as the row (or column) order of matrix A.
     node: Label of a specific node.
     
    '''
    G = nx.Graph()
    for k in range(len(nodes)):
       node_label=nodes[k]
       G.add_node(node_label, desc=node_label)
    for i in range(len(A)):
       for j in range(len(A)):
           if A[i][j]>0:
              G.add_edge(nodes[i],nodes[j])
    Neighbors=list(G.neighbors(node))
    for k in range(len(nodes)):
        if (nodes[k] not in Neighbors) and (nodes[k] != node):
            G.remove_node(nodes[k])
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color='b')
    nx.draw_networkx_nodes(G, pos, nodelist=node, node_color='r')
    node_labels = nx.get_node_attributes(G, 'desc')
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    nx.draw_networkx_edges(G, pos,edge_color='y',width=1)
    plt.show()
############################################################           

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
loc_net(A,nodes,'K')
















