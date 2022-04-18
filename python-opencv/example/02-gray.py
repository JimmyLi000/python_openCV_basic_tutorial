#---02讀取灰階---

import cv2

img = cv2.imread('D:/python_cv-ex/ex01/lena.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
