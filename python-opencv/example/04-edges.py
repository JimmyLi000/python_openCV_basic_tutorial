 #---04邊緣偵測---

import cv2
import numpy as np

#用灰階模式讀取RGB影像
img = cv2.imread("D:/python_cv-ex/ex01/lena.jpg",0) 
edges = cv2.Canny(img, 100, 200)
cv2.imshow("edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()