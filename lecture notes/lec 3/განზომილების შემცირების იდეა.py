import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=1000, n_features=10, n_informative=2, n_redundant=8, random_state=1)
''' 
x არის მატრიცა 1000x10,
y არის სვეტი, შედგება 0 და 1-სგან არის 1000x1-ზე,ანგარიშობს შედეგს, ან არის ან არა
samples რიგი, features სვეტი, 
informative რამდენია მნიშნველოვანი, redundant - ზედმეტი
'''
data = pd.DataFrame(X, columns=['Feature'+str(i) for i in range(10)])
print(data.corr()) # კორელაციის მატრიცა, რამდენი სვეტიცაა იმდენი რიგია