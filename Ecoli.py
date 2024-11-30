import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as s
from sklearn.linear_model import LinearRegression


def readfile(path, filename):  # Read text file and create edge list
    f = open(path + filename, 'r+')
    doc = [line[:-1] for line in f.readlines()]
    f.close()
    edge = []
    for i in range(0, len(doc)):
        d_edge = doc[i].split(' ')
        d_edge = [int(d_edge[0]), int(d_edge[1])]
        edge.append(d_edge)
    edge = sorted(edge)
    return edge


def diameter(G):
    all_max = []
    for i in range(0, len(nodes)):
        s = nodes[i]
        short_path_in_node = []
        for j in range(i, len(nodes)):
            t = nodes[j]
            if nx.has_path(G, source=s, target=t):
                s_length = nx.shortest_path_length(G, source=s, target=t)
                short_path_in_node.append(s_length)
        max_short_path_in_node = max(short_path_in_node)
        all_max.append(max_short_path_in_node)
    d = max(all_max)
    return d


def distribution(G):
    deg_list = list(sorted(G.degree))  # Sort of Degree
    deg = [deg_list[i][1] for i in range(0, len(deg_list))]  # get just Degree
    unique_degree = sorted(list(dict.fromkeys(deg)))  # get Unique degree
    total = len(nodes)
    count_of_degree = []
    Pk = []
    c = []
    pk = []
    # Calculate the Probability of Degree
    for i in range(0, len(unique_degree)):
        for j in range(0, len(deg)):
            c = deg.count(unique_degree[i])
            pk = c / total
        count_of_degree.append(c)
        Pk.append(pk)
    # figure for degree distribution
    plt.plot(count_of_degree, unique_degree, 'o')
    plt.xlabel('Count of Degree')
    plt.ylabel('Unique Degree')
    plt.title('Degree Distribution')
    plt.show()
    return unique_degree,Pk


def plot_distribution(unique_degree,Pk,a,b):
    # convert to loglog format
    unique_degree = np.log2(unique_degree[a:b])
    Pk = np.log2(Pk[a:b])
    # Investigate of Correlation
    correlation, p_value = s.pearsonr(unique_degree, Pk)
    # Linear Regression
    [gama,b] = np.polyfit(unique_degree, Pk, 1)
    y = [gama* unique_degree[i] + b for i in range(0, len(unique_degree))]
    # figure degree distribution loglog for P(k)
    plt.plot(unique_degree, Pk, 'o')
    plt.plot(unique_degree, y, c='r')
    plt.xlabel('Degree. Log2(k)')
    plt.ylabel('Probability of Degree. Log2(f(k))')
    plt.title('Degree Distribution')
    plt.text(2.5, -5.4, 'gama : ')
    plt.text(3.5, -5.4, gama)
    plt.show()
    return gama,correlation,p_value


def plot_cumulative(unique_degree,Pk,a,b):  # Cumulative distribution
    # convert to loglog format
    unique_degree = np.log2(unique_degree[a:b])
    # Cumulative Process
    Fck = np.cumsum(Pk)
    Fck = [1 - Fck[i] for i in range(0,len(Fck))]
    Fck = np.log2(Fck[a:b])
    # Investigate of Correlation
    correlation2, p_value2 = s.pearsonr(unique_degree, Fck)
    # Linear Regression
    [gama2, b2] = np.polyfit(unique_degree, Fck, 1)
    y = [gama2 * unique_degree[i] + b2 for i in range(0, len(unique_degree))]
    # figure of  Cumulative Probability distribution loglog for Fc(k)
    plt.plot(unique_degree, Fck, 'o')
    plt.plot(unique_degree, y, c='r')
    plt.xlabel('Degree. Log2(k)')
    plt.ylabel('Cumulative Probability of Degree. Log2(Fc(k))')
    plt.title('Cumulative Degree Distribution')
    plt.text(3.2, -4, 'gama : ')
    plt.text(4.1, -4, gama2)
    plt.show()
    return gama2,correlation2,p_value2


def cluster_coefficient(G):
    clustering_coefficient_list = []
    for i in range(0, len(nodes)):  # we search and calculate cluster coefficient for any nodes
        neighbor = list(nx.neighbors(G, nodes[i]))  # connected nodes with choose node
        ni = len(neighbor)
        if ni > 1:
            mi = 0
            for j in range(0, len(neighbor)):
                for k in range(0, len(neighbor)):
                    if neighbor[j] in list(nx.neighbors(G, neighbor[k])):
                        mi += 1
            mutual = mi / 2  # we have to divide in 2 for repetition
            cc = (2 * mutual) / (ni * (ni - 1))  # clustering coefficient formula (Eq : 4.12 from book)
        else:
            cc = 0  # Because degree less than 2
        clustering_coefficient_list.append(cc)  # all of nodes cc collect to in list
    clustering_coefficient = (sum(clustering_coefficient_list)) / len(nodes)
    return clustering_coefficient


# Initialize :
path = 'F:/fati/arshad/3/data mining\saghafi-HW2/'
filename = 'Ecoli.txt'
edge = readfile(path,filename)
G = nx.Graph()
G.add_edges_from(edge)
nodes = list(sorted(nx.nodes(G)))
print('Number of Nodes:',len(nodes))
print('Number of Edges:',len(edge))

""""""""""""""""""""""" Answer 1-1 : Diameter Calculation """""""""""""""""""""""""""""
d = diameter(G)
print('******************************** Answer 1-1 : ********************************')
print('Diameter : ', d)
""""""""""""""""""""""" Answer 1-2 : Degree Distribution Calculation"""""""""""""""""""""""""""
print('******************************** Answer 1-2 : ******************************** ')
[unique_degree,Pk] = distribution(G)
[gama,correlation,p_value] = plot_distribution(unique_degree,Pk,0,len(Pk))
print('Correlation for Probability Distribution : ',correlation)
print('P_Value for Probability Distribution : ',p_value)
print('gama for Probability Distribution : ',gama)
[gama2,correlation2,p_value2] = plot_cumulative(unique_degree,Pk,1,-2)
print('Correlation for Cumulative Probability Distribution : ',correlation2)
print('P_Value for Cumulative Probability Distribution : ',p_value2)
print('gama for Cumulative Probability Distribution : ',gama2)

""""""""""""""""""""""" Answer 1-3: Cluster Coefficient Calculation """""""""""""""""""""""""""
cc = cluster_coefficient(G)
print('******************************** Answer 1-3 : ********************************')
print('Clustering Coefficient : ', cc)
#print('Networkx Package answer : ',nx.average_clustering(G,nodes))  # for evaluation
