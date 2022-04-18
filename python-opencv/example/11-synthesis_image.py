 #---11. 影像合成一張---

import cv2
import numpy as np
img1 = cv2.imread('D:/python_cv-ex/ex01/lena.jpg')
img2 = cv2.imread('D:/python_cv-ex/ex01/lena.jpg')
tmp = np.hstack((img1,img2))

cv2.imshow("img",tmp)
cv2.waitKey(0)
cv2.destroyAllWindows()
