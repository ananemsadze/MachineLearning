import numpy as np
from numpy.linalg import norm
from numpy import inf
from scipy.spatial import distance

## ვექტორების ჯამი

# a = np.array([2, 3, 1])
# b = np.array([1, 2, 5])
#
# c = a + b
# c1 = a - b
# print(c)
# print(c1)


#####################
## სკალარული ნამრავლი

# a = np.array([2, 2, 3])
# b = np.array([1, 2, -2])
# scalar_product = np.dot(a, b)
# print(scalar_product)


#####################
## L2 რიგის ნორმა, ვექტორის სიგრძე


# u = np.array([1,2,3])
# norm1 = norm(u)
# print(norm1)

## L2 რიგის ნორმა, აბსოლუტური მნიშვნელობების ჯამი
# u = np.array([-1,-2,3])
# norm1 = norm(u,1)
# print(norm1)

## L0 რიგის ნორმა, არანულოვან წევრთა რაოდენობა
# a = np.array([1, 3, 0, 2])
# print(np.count_nonzero(a))

## უსასრულო რიგის ნორმა

# u = np.array([-1, -2, 3])
# norm1 = norm(u, inf)
# print(norm1)


#####################
# ორ ვექტორს შორის მანძილი (იგივეა რაც მათი სხვაობით მიღებული ვექტორის სიგრძე)

# a = np.array([1,3])
# b = np.array([2,4])
# distance = norm(b-a)
# print(distance)


## იგივე სხვა scipy-თი
# a = np.array([1,3])
# b = np.array([2,4])
# dst = distance.euclidean(a, b)
# print(dst)


#####################
## ორ ვექტორს შორის კუთხე (მათი სკალარული ნამრავი გაყოფილი მათი სიგრძეების ნამრავლზე)
# u = np.array([2, 2])
# v = np.array([0, 3])
#
#
# product = np.dot(u, v)
# normu = np.linalg.norm(u)
# normv = np.linalg.norm(v)
# cost = product / (normu * normv)
# print(cost)
# print(math.degrees(math.acos(cost)))
