from glob import glob
#remove this line
START = 447767
END = 19800001
NUMTOK =272602
#remove this line
TOT = END-START
mask = np.arange(0, TOT,6500)



def processFile(filename):
    #remove these lines with counter
    _temp = np.load(filename)['arr_0']
    __temp = np.cumsum(_temp)[mask]
    overall=np.diff(__temp)
    np.savez(filename.replace('npys','diffnpys'), overall)
    print('Processed ', filename)    


with futures.ProcessPoolExecutor(max_workers=48) as ex:
    for _filename in  glob('npys/*'):
        ex.submit(processFile, _filename)
    print('******MAIN******: closing')