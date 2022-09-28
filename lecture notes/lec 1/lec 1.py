"""

https://gist.github.com/curran/a08a1080b88344b0c8a7

[] vector
[[]] matrix
[[[]]] tensor
რამდენო [] იმდენი განზომილებაა.
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd

v = np.array([5.1, 3.5, 1.5, 6.2])
w = np.array([4.9, 3.0, 1.4, 0.2])
distance = np.linalg.norm(w - v)  # distance between them
print(distance)

#################################
# matrix is with upper letters

A = np.array([[2, 1, 3], [0, 4, 5], [6, 7, 8]])  # matrix
print(A)

#################################


color_image = cv2.imread("1.png")
plt.imshow(color_image)
plt.show()
print(color_image)  # prints matrix
print(color_image.shape)  # bgr - color channels, three numbers


###############
data = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")
print(data.values) # prints iris dataset matrix