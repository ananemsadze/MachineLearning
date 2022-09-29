import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder

myconverter = LabelEncoder()  # converts data into numbers

# without converter the output was ['setosa' 'versicolor' 'virginica']

data = pd.read_csv(
    "https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")
data['species'] = myconverter.fit_transform(data['species'])  # check each info and then convert it

# converted data equals to [0 1 2]

# print(data.head())
# print(data["species"].unique())

# X uppercase, y lowercase
X = data.drop("species", axis=1).values
# write everything in x after dropping the column "species", axis სვეტი, ამოიღოს მხოლოდ მნიშვნელობები ანუ 0,1,2
y = data['species'].values

# print(X)  # ორგანზომილებიანი მატრიცა

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.99,
                                                    random_state=4)  # stratify-ის პროცენტულობით გაყოფს, ყოველთვის y-ით იწერება
# random state - რომლიდან დაიწყოს
from sklearn.neighbors import KNeighborsClassifier

mymodel = KNeighborsClassifier(n_neighbors=1)
mymodel.fit(X_train, y_train)
# print(mymodel.score(X_test, y_test)) # overwriting, test is lower
# print(mymodel.score(X_train, y_train))



