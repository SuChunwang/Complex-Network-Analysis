import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def modularity_matrix(A):
    """
    The modularity matrix is the matrix B = A - <A>, where A is the adjacency
    matrix and <A> is the average adjacency matrix, assuming that the graph
    is described by the configuration model.

    More specifically, the element B_ij of B is defined as
        A_ij - k_i k_j / 2 * m
    where k_i(in) is the degree of node i, and were m is the number of edges
    in the graph. When weight is set to a name of an attribute edge, Aij, k_i,
    k_j and m are computed using its value.

    Returns
    -------
    B : Numpy matrix
      The modularity matrix of the graph.
      
    References
    ----------
    .. [1] M. E. J. Newman, "Modularity and community structure in networks",
       Proc. Natl. Acad. Sci. USA, vol. 103, pp. 8577-8582, 2006.
    """

    k = A.sum(axis=1)
    m = k.sum() * 0.5
    # Expected adjacency matrix
    X = k * k.transpose() / (2 * m)
    return A - X


def partition(B):
    e_vals,e_vecs = np.linalg.eig(B)
    print('特征值：\n',e_vals)
    print('特征向量矩阵：\n',e_vecs)
    leading_eigenvector = e_vecs[:,0]
    print('主特征向量：\n',leading_eigenvector)
    s = np.sign(leading_eigenvector)
    print('归属状态：\n',s)
    List1=[]
    List2=[]
    List3=[]
    for i in range(len(s)):
        if s[i]>0:
            List1.append(i)
        elif s[i]<0:
            List2.append(i)
        else:
            List3.append(i)
    print('社团划分：\n','社团一：',List1,'\n','社团二：',List2)
    return List1,List2

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
B = modularity_matrix(A)
L1,L2 = partition(B)
nodes = ['A','B','C','D','E','F','G','H','I','J','K']
color1 = 'r'
color2 = 'b'
color3 = 'g'
nodes_col = []
G = nx.Graph()
for k in range(len(nodes)):
    node_label=nodes[k]
    G.add_node(node_label, desc=node_label)
    if k in L1:
        nodes_col.append(color1)
    elif k in L2:
        nodes_col.append(color2)
    else:
        nodes_col.append(color3)
for i in range(len(A)):
    for j in range(len(A)):
        if A[i][j]>0:
           G.add_edge(nodes[i],nodes[j])
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color=nodes_col)
node_labels = nx.get_node_attributes(G, 'desc')
nx.draw_networkx_labels(G, pos, labels=node_labels)
nx.draw_networkx_edges(G, pos,edge_color='y',width=2)
plt.show()



























