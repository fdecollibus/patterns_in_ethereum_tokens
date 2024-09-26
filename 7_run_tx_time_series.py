import pickle
import zarr
import csv
from glob import glob
subdic,revdic= pickle.load(open('dictionary_token_red.pickle','rb'))
import numpy as np
#remove this line
START = 447767
END = 19800001
NUMTOK =14906
#remove this line
TOT = END-START
mask = np.arange(0, TOT,6500)

counter = 0
overall=np.zeros([NUMTOK,len(mask)-1])
for _file in glob('diffnpys/*'):
    print(_file)
    token = _file.split('/')[-1].split('.')[0]
    if token in subdic.keys():
        counter += 1
        idtoken= subdic[token]
        print(token, idtoken)
        #remove these lines with counter
        _temp = np.load(_file)['arr_0']
        #print(_z,mask[_z]
        overall[idtoken]=_temp
np.save('diff_results_new.npy', overall)
print('added tokens', counter)
