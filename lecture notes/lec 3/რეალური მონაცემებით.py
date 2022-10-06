import numpy as np
import pandas as pd

data = pd.read_csv(
    "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")
# print(data.head())

print(data['variety'].unique())  # დაპრინტავს 'setosa' 'versicolor' 'virginica'

mapping = {"Setoda": 0, "Versicolor": 1, "Virginica": 2}  # წინა მონაცემებს გადაიყვანს რიცხვებში
data['variety'] = data['variety'].map(mapping)  # მაპავას

X = data.drop("variety", axis=1).values  # x-ში ამოვა ყველა ოთხი სვეტის მნივნელობა variety-ის გათვალისწინების გარეშე
y = data["variety"].values

print(X.shape)  # გამოვა 150x4-ზე

from sklearn.model_selection import train_test_split  # განზომილების შემცირებისთვის

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)  # 150-ის 20 პროცესი ტესტისთვის
from sklearn.decomposition import PCA  # ამ ოთხი სვეტიდან რამდენი ახალი სვეტი შექმნას

mypca = PCA(n_components=1)  # რამდენი ახალი სვეტი მიიღოს, შეიქმენა 1 ახალი

X_train = mypca.fit_transform(X_train)  # თავდაპირველი 4 სვეტისგან მივიღებთ 1-ს
X_test = mypca.transform(X_test)

print(X_train.shape)  # 120, 1-ზე, აიღო 150-ის 20 პროცენტი
print(
    mypca.explained_variance_ratio_)  # აჩვენებს თუ ერთმა სვეტმა რამდენი ინფო მიიზიდა თავდაპირველი სვეტისგან, 0.92 შეინარჩუნა

from sklearn.neighbors import  KNeighborsClassifier
mymodel = KNeighborsClassifier()
mymodel.fit(X_train, y_train)
# print(mymodel.score(X_test, y_test))