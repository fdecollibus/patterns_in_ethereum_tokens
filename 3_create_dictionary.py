from glob import glob
#Create  a dictionary of tokens to be later used to index arrays
import pickle
subdic = dict() 
revdic = dict()
def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return sum(1 for line in f)
for _file in glob('token_data/0x*/ordered_token_transfer.csv'):
    print(_file)
    subdic[_file.split('/')[-2]]=len(subdic)
    revdic[subdic[_file.split('/')[-2]]]=_file.split('/')[-2]
pickle.dump([subdic,revdic],open('dictionary_token.pickle','wb'))
