from asyncore import read
from typing import IO
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate
from surprise import SVD

import pandas as pd
class Evaluator():
    
    algorithms = []

    def __init__(self, datasetpath):
        # path to dataset file
        file_path = datasetpath
        #open our file, load it into a pandas dataframe and then load that dataframe into a Surprise dataset.
        try:
            file = open(file_path,'rb',0)
            data = pd.read_csv(file_path,header=0,encoding = "ISO-8859-1",sep=';')
            reader = Reader(rating_scale=(0,10))
            file.close()
            self.dataset = Dataset.load_from_df(data, reader)
        except IOError:
            print("File not found")

    def evaluate(self):
        pass
    
    def addAlgorithm(self, algorithm):
        self.algorithms.append(algorithm)
        
        




# now we can start evaluating against algorithms.

