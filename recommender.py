import csv
from surprise import BaselineOnly
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate
import csv
# path to dataset file
file_path = ("book-review-dataset/BX-Book-Ratings.csv")

# As we're loading a custom dataset, we need to define a reader. In the
# movielens-100k dataset, each line has the following format:
# 'user item rating timestamp', separated by '\t' characters.

with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='"')
    for row in reader:
        print(', ')

#data = Dataset.load_from_file(file_path, reader=reader)

# We can now use this dataset as we please, e.g. calling cross_validate
cross_validate(BaselineOnly(), data, verbose=True)
