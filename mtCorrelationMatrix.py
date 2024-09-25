import numpy as np
import concurrent.futures
from scipy.stats import spearmanr

# Assuming 'test' is your matrix of data
#test = np.random.rand(10, 100)  # Example data
test = np.load('diff_results_new.npy')
results = np.zeros((len(test), len(test), 3))  # Storing correlations, p-values, and counts
import pickle
dic,revdic = pickle.load(open('dictionary_token_red.pickle','rb'))
def process_row(t):
    print('Processing ',t, revdic[t])
    local_results = []
    for r in range(len(test)):
        if (np.sum(test[t]) > 0) and (np.sum(test[r]) > 0):
            index = max(np.where(test[t] > 0)[0][0], np.where(test[r] > 0)[0][0])
            if r > 0:  # Ensure r-1 doesn't go out of index
                correlation, p_value = spearmanr(test[r-1][index:], test[r][index:])
            else:
                correlation, p_value = 0, 1  # Default or handle edge case differently
            mask1 = test[t] > 0
            mask2 = test[r] > 0
            combined_mask = mask1 & mask2
            count = np.sum(combined_mask)
            local_results.append((correlation, p_value, count))
        else:
            local_results.append((0, 1, 0))  # Default values for cases with no valid data
    return t, local_results

# Using ThreadPoolExecutor to manage multithreading
with concurrent.futures.ThreadPoolExecutor(max_workers=64) as executor:  # Adjust number of workers as needed
    future_to_row = {executor.submit(process_row, t): t for t in range(len(test))}
    for future in concurrent.futures.as_completed(future_to_row):
        t, local_results = future.result()
        for r in range(len(test)):
            results[r][t][0] = local_results[r][0]
            results[r][t][1] = local_results[r][1]
            results[r][t][2] = local_results[r][2]

np.savez_compressed('results.npz', results=results)
print("Processing complete and data saved.")
