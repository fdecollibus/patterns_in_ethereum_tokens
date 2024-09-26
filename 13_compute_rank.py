
# This script covers section 3.5 of the paper
import pickle
import random
import numpy as np

# Define the range of alpha values to try
alpha_try_values = np.arange(0.5, 2.2, 0.05)

# Initialize the rank function dictionary
rank_function = {}

# Load the temporary file
overall = np.load('cumsum_results_cs.npz')['cumsums']
print(f"Overall shape: {overall.shape}")

# Determine the number of samples by dividing the last cumulative sum by 1000
SAMPLES = np.sum(overall[:, -1]) / 1000

# Initialize the rank function arrays with slighly more space than required
for _a in alpha_try_values:
    rank_function[_a] = np.zeros(int(SAMPLES * 1.25))

print(f"Sample shape for alpha={alpha_try_values[-1]}: {rank_function[alpha_try_values[-1]].shape}")

for _r in range(overall.shape[1] - 2):
    # Calculate the new and destination degrees
    new = overall[:, _r][overall[:, _r+1] - overall[:, _r] > 0]
    dest_degree = np.sort(new[new > 0])
    counting_nodes = (overall[:, _r+1] - overall[:, _r])[overall[:, _r+1] - overall[:, _r] > 0]
    for dest_degree, counting_nodes in zip(new1[new1>0],new2[new1>0]):
        for _z in range(0,int(counting_nodes)):
            #Sampling only with a specific likelihood
            if random.random()<0.00011:
                for _a in alpha_try_values:
                    degrees_alpha = degrees**_a
                    partial_degrees_alpha1 = degrees_alpha[degrees < dest_degree]
                    partial_degrees_alpha2 = degrees_alpha[degrees == dest_degree]
                    rank_function[_a][counter] = (np.sum(partial_degrees_alpha1) + np.sum(partial_degrees_alpha2))/np.sum(degrees_alpha)
#Saving the file for further analysis
pickle.dump(rank_function, open('rank_function_token_24.pickle','wb'))

