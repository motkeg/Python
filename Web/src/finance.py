import pandas as pd

import numpy as np

from sklearn.naive_bayes  import GaussianNB  #need 2.7 version



df= pd.read_csv("table.csv")
print (df)