 #---07. cv2圖片旋轉---

import cv2
import numpy as np
img = cv2.imread('D:/python_cv-ex/ex01/lena.jpg')

(h,w) = img.shape[:2]
center = (w/2,h/2)

angle = 60
M = cv2.getRotationMatrix2D(center, angle, 1.0)
roated_img = cv2.warpAffine(img, M, (w,h))

cv2.imshow("img",roated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()