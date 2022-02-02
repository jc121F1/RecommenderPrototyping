from asyncore import read
import itertools
from subprocess import SubprocessError
from termios import FIONBIO
from xml.etree.ElementTree import tostring
from surprise import BaselineOnly
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate
from surprise import SVD
import pandas as pd
from pandas import Series
from pandas import DataFrame

# path to dataset file
file_path = ("book-review-dataset/BX-Book-Ratings.csv")

# As we're loading a custom dataset, we need to define a reader. In the
# movielens-100k dataset, each line has the following format:
# 'user item rating timestamp', separated by '\t' characters.
file = open(file_path,'rb',0)

data = DataFrame(pd.read_csv(file_path,header=0,encoding = "ISO-8859-1",sep=';'))
data = data.astype({"User-ID" : int, "ISBN" : str, "Book-Rating":int})
reader = Reader(rating_scale=(0,10))

dataset = Dataset.load_from_df(data, reader)

counts = data.value_counts(subset = 'ISBN')

book_file_path = ("book-review-dataset/BX_Books.csv")

bookdata = DataFrame(pd.read_csv(book_file_path, header=0, encoding= "ISO-8859-1", sep=';'))

i = 0


# convert our series of isbn,counts into a list of tuples, then take only the first ten
counts = list(counts.items())
counts = counts[:10]
# for each isbn and count, print the count, then find the relevant row in the book csv and print it out
for name, count in counts:
    
    row = bookdata.loc[bookdata['ISBN'] == name, ['ISBN', 'Book-Title']]
    if not(row.empty):
        print("Recommendations: " + str(count) + " for " + row['Book-Title'])
        print(" --- ")

#algo = SVD()

# We can now use this dataset as we please, e.g. calling cross_validate

#cross = cross_validate(algo, dataset, verbose=True, n_jobs=-1)
