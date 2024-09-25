import csv,time,glob
import pandas as pd,os
from datetime import datetime
import traceback
import numpy as np
import pickle

blockToTimestamp = dict()
timestampToBlock = dict()
start =time.time()

def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return sum(1 for line in f)

def alph_order(a: str, b: str) -> str:
    return a.lower() + '_' + b.lower() if a.lower() < b.lower() else b.lower() + '_' + a.lower()

print('Preparing block list')
with open('aggregate/block_timestamp.csv') as f:
    reader = csv.reader(f)
    for line in reader:
        blockToTimestamp[int(line[0])]=int(line[1])
        timestampToBlock[int(line[1])]=int(line[0])
print ("time elapsed {}".format(time.time()-start))
print(len(blockToTimestamp))
print(len(timestampToBlock))


#Change the path where you have ordered token transfers
filenames = glob.glob("token_data/0x*/ordered_token_transfer.csv")
print("There are {} to be scanned".format(len(filenames)))

total_number=0


#Create a set of nodes and edges for each file and store them in a pickle file on the same path
for filename in filenames:
    if count_lines(filename)>10000:
        new_nodes=set()
        new_edges=set()
        total_number+=1
        print("Analyzing token in {}".format(filename))
        outr=open(filename,'r')
        reader =csv.DictReader(outr)
        for line in reader:
            new_nodes.add(line['from_address'])
            new_nodes.add(line['to_address'])
            new_edges.add(alph_order(line['from_address'],line['to_address']))
        pickle.dump(new_edges,open(filename.rstrip('ordered_token_transfer.csv') + 'set_edges.pickle','wb'))
        pickle.dump(new_nodes,open(filename.rstrip('ordered_token_transfer.csv') + 'set_nodes.pickle','wb'))
print("total processed ", total_number)
