import numpy as np
import pandas as pd
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import adfuller
from statsmodels.tools.eval_measures import rmse, aic
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import arma_order_select_ic

import pickle
import zarr
import csv
from glob import glob
#Dictionary token address to id
subdic,revdic= pickle.load(open('dictionary_token.pickle','rb'))
import numpy as np
# the first 447767 blocks nothing happen, we can save some space
START = 447767
END = 19800001
NUMTOK =1178664
#remove this line
TOT = END-START

counter = 0
processed = set()
overall=np.zeros([NUMTOK,2977])
parameters = np.zeros([1178664,8],dtype=int)

for _file in glob('npys/*.npz'):
    try:
        print(_file)
        token = _file.split('/')[-1].split('.')[0]
        idtoken= subdic[token]
        processed.add(idtoken)
        print(token, idtoken)
        #remove these lines with counter
        array1 = np.load(_file)['arr_0']
        print(array1)
        if len(array1) % 6500 != 0:
            array1 = array1[:-(len(array1) % 6500)]
        # Reshape the array
        reshaped_array = array1.reshape(-1, 6500)
        summed_blocks = reshaped_array.sum(axis=1)
        if np.sum(summed_blocks)>10000:
            overall[idtoken]=summed_blocks
            indices = np.argwhere(summed_blocks != 0)
            first_index = int(indices[0])
            print(first_index)
            last_index = int(indices[-1])
            print(last_index)
            array=summed_blocks[first_index:last_index]
            res = arma_order_select_ic(array, max_ar=5, max_ma=5, ic=['aic', 'bic', 'hqic'])
            # The parameters we select for the token id, resp. AIC, BIC, HQIC and the first and last occurrence of token's activity
            parameters[idtoken] = [res.aic_min_order[0],res.aic_min_order[1], res.bic_min_order[0],res.bic_min_order[1], res.hqic_min_order[0],res.hqic_min_order[1],first_index,last_index]
    except:
        print('Problem with ', _file )
        continue
#We save the temporary file for further processing
np.savez_compressed('results_cs_24.npz', parameters=parameters, overall=overall)
