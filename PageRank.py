import networkx as nx
import numpy as np
# Function


def readfile(path, filename):  # Read text file and create edge list
    f = open(path + filename, 'r+')
    doc = [line[:-1] for line in f.readlines()]
    doc
    f.close()
    edge = []
    for i in range(0, len(doc)):
        d_edge = doc[i].split(' ')
        d_edge = [int(d_edge[0]), int(d_edge[1])]
        edge.append(d_edge)
    edge = sorted(edge)
    return edge


def page_rank(G,d,threshold):  # Page rank function: input value-->
    # G: directed graph,
    # d: probability 0.1 we follow a random link,
    # threshold: difference between the old and the new scaled vector threshold
    nodes = list(sorted(nx.nodes(G)))  # Get Nodes
    out_deg_list = G.out_degree(nodes)  # Get out-degree of any node in list
    N = np.zeros([len(nodes), len(nodes)])  # N template
    for i in range(0, len(edge)):  # Create N matrix
        e = edge[i]
        ou = out_deg_list[e[0]]
        if ou == 0:
            n = 0
        else:
            n = 1 / ou
        N[e[0]][e[1]] = n
    Nr = (1 / len(nodes)) * np.ones([len(nodes), len(nodes)])  # Create Nr matrix
    M = ((1-d) * N) + (d * Nr)  # Create M matrix
    M_t = np.transpose(M)  # Transpose M Matrix
    p0 = np.ones([len(nodes), 1])  # Initial P0
    condition = False
    eigenvector = []
    eigenvalue = []
    pn_vector = []
    i = 0
    while not condition:
        pn = np.array(np.dot(M_t, p0))  # Create Pn Iteration
        max_pn = max(pn)
        index_i = np.where(pn == max_pn)  # find max argument
        landa = pn[index_i] / p0[index_i]  # Eigenvalue Estimate
        delta = np.sqrt(sum(np.power(np.array(pn) - np.array(p0), 2)))  # calculate Error
        p0 = pn  # Replace for next iteration
        if delta < threshold:  # Condition for Stop Iteration
            condition = True
            eigenvalue = landa  # Replace landa to eigenvalue
            eigenvector = np.ravel(pn/max_pn)  # Normalization of eigenvector

    eigenvector_dct = {i: eigenvector[i] for i in range(0, len(eigenvector))}  # create eigenvector dictionary, Key:node
    sort_eigen_vector = dict(sorted(eigenvector_dct.items(), key=lambda item: item[1]))  # sort eigenvector dictionary
    sort_eigen_vector_list = list(sort_eigen_vector)[::-1]  # Descending sort to get top 10
    top_10 = sort_eigen_vector_list[0:10]
    top_10_value = [eigenvector_dct[i] for i in top_10]
    top_10_gene = {top_10[i]: top_10_value[i] for i in range(0, len(top_10))}
    return eigenvalue,eigenvector, top_10_gene


# Initialize
path = 'F:/fati/arshad/3/data mining\saghafi-HW2/'
filename = 'Ecoli_directed.txt'
#edge = readfile(path, filename)
#G = nx.DiGraph()  # create directed graph
#G.add_edges_from(edge)  # add Edge to the graph
#[eigenvalue,eigenvector, top_10_gene] = page_rank(G,0.1,0.001)
#print('Page Rank Function Result : ')
#print('eigenvalue : ', eigenvalue)
#print('eigenvector : ', eigenvector)
#print('top_10_gene : ', top_10_gene)
