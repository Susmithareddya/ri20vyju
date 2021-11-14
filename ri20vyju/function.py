import sys
!{sys.executable} -m pip install opencv-python
import cv2
import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
import matplotlib.pyplot as plt
def imshow(X, nR, nC):
    number_rows = len(X)     # source number of rows 
    number_columns = len(X[0])  # source number of columns 
    print(number_columns)
    print(number_rows)
    return [[ X[int(number_rows * r / nR)][int(number_columns * c / nC)]  
                 for c in range(nC)] for r in range(nR)]
pass
X = cv2.imread('C:\\Users\\susmi\\Desktop\\Dss assignments\\EX2\\home.jpg')
res = imshow(X, 30, 30)
plt.imshow(res)
