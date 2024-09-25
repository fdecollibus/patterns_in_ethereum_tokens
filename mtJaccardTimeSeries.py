import csv
import glob
import os
import pickle
import concurrent.futures
from datetime import datetime
import traceback
import numpy as np
import pandas as pd

def jaccard_index(set1, set2):
    intersection_len = len(set1.intersection(set2))
    union_len = len(set1.union(set2))
    return intersection_len / union_len

def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return sum(1 for line in f)

def process_file(filename):
    try:
        print('Processing ', filename)
        results = {}
        address_from = filename.split("/")[-2]
        if os.path.exists(f'tmp/temp_{address_from}.pickle'):
            print(address_from , ' already exists, skipping')
        transactions = count_lines(filename.replace('set_edges.pickle','ordered_token_transfer.csv'))
        set_from_edges = pickle.load(open(filename,'rb'))
        set_from_nodes = pickle.load(open(filename.replace('edges','nodes'),'rb'))
        num_edges = len(set_from_edges)
        num_nodes = len(set_from_nodes)

        results['transactions'] = transactions
        results['num_edges'] = num_edges
        results['num_nodes'] = num_nodes
        results['nodes'] = {}
        results['edges'] = {}

        for subfilename in glob.glob("token_data/0x*/set_edges.pickle"):
            address_to = subfilename.split("/")[-2]
            if address_to != address_from :
                set_to_edges = pickle.load(open(subfilename, 'rb'))
                set_to_nodes = pickle.load(open(subfilename.replace('edges','nodes'),'rb'))
                results['nodes'][address_to] = jaccard_index(set_from_nodes, set_to_nodes)
                results['edges'][address_to] = jaccard_index(set_from_edges, set_to_edges)
        # Serialize results to a unique temporary file
        temp_filename = f'tmp/temp_{address_from}.pickle'
        pickle.dump(results, open(temp_filename, 'wb'))
        return temp_filename

    except Exception as e:
        print(f"Error processing {filename}: {e}")
        traceback.print_exc()

def merge_results(filenames):
    all_results = []
    for file in filenames:
        with open(file, 'rb') as f:
            all_results.append(pickle.load(f))
        #os.remove(file)  # Optionally remove the temp file after merging
    # You can process all_results here, or dump it again into one final results file
    pickle.dump(all_results, open('mt_final_results_jaccard.pickle', 'wb'))

filenames = glob.glob("token_data/0x*/set_edges.pickle")
print(f"There are {len(filenames)} files to be scanned")

# Create a thread pool and process files
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    futures = [executor.submit(process_file, filename) for filename in filenames]
    temp_files = [future.result() for future in concurrent.futures.as_completed(futures)]

# Merge all temporary files into a final results file
merge_results(temp_files)

print("All files have been processed and results are merged.")

