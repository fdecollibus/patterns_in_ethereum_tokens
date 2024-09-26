import pickle
import zarr
import csv
from glob import glob
subdic,revdic= pickle.load(open('dictionary_token.pickle','rb'))
import numpy as np
#adapt these values accordingly
START = 447767
END = 19800001
NUMTOK =1178664
TOT = END-START
mask = np.arange(0, TOT,6500)

counter = 0
processed = set()
overall=np.zeros([NUMTOK,2977])
for _file in glob('npys/*'):
    try:
        print(_file)
        token = _file.split('/')[-1].split('.')[0]
        idtoken= subdic[token]
        processed.add(idtoken)
        print(token, idtoken)
        array1 = np.load(_file)['arr_0']
        print(array1)
        if len(array1) % 6500 != 0:
            array1 = array1[:-(len(array1) % 6500)]
        # Reshape the array
        reshaped_array = array1.reshape(-1, 6500)
        summed_blocks = reshaped_array.sum(axis=1)
        overall[idtoken]=summed_blocks
    except Exception as e:
        # todo: Handle the exception
        print(f"An error occurred: {e}")
cumulative_sums = np.cumsum(overall, axis=1)
np.savez('cumsum_results_cs.npz',cumsums=cumulative_sums)
