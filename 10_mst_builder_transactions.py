import pickle
import scipy.stats
import pandas as pd
import numpy as np
import math
import networkx as nx

# Load the results from the previous step
matrix = np.load('results.npz')['results']
dicred,subred = pickle.load(open('dictionary_token_red.pickle','rb'))
matrix[0][matrix[1]>0.05]=0
matrix[0][matrix[2]<30]=0

corr_network=nx.Graph()

num_added=0
num_jumped=0
for _fromkey in range(0,len(matrix)):
    for _tokey in range(0,len(matrix)):
        if _fromkey!= _tokey:
            metric_distance=1 - matrix[:,:,0][_fromkey][_tokey]**2
            if not corr_network.has_edge(subred[_fromkey],subred[_tokey]):
                corr_network.add_edge(subred[_fromkey],subred[_tokey], weight=metric_distance)
                num_added+=1
            else:
                num_jumped+=1
        

        
print("number of nodes:",corr_network.number_of_nodes())
print("number of edges:",corr_network.number_of_edges())
nx.write_graphml(corr_network,'temp_transactions_fixed_24.graphml')
tree_seed=subred[random.randint(0, len(matrix))]
print(tree_seed)
counter = 0
N_new=[]
E_new=[]
N_new.append(tree_seed)
while len(N_new)<corr_network.number_of_nodes():
    min_weight=10000000.0
    for n in N_new:
        for n_adj in corr_network.neighbors(n):
            if not n_adj in N_new:
                if corr_network[n][n_adj]['weight']<min_weight:
                    min_weight=corr_network[n][n_adj]['weight']
                    min_weight_edge=(n,n_adj)
                    n_adj_ext=n_adj
    E_new.append(min_weight_edge)
    N_new.append(n_adj_ext)
    counter += 1
    if (counter % 100 == 0):
        print ('added ', counter)

#generate the tree from the edge list
tree_graph=nx.Graph()
tree_graph.add_edges_from(E_new)
nx.write_graphml(tree_graph,'mst_transactions_fixed_24.graphml')
#Then we have to apply Prim's algorithm to find the minimum spanning tree