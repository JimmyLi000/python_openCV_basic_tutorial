 #---03二值化---

import cv2

img = cv2.imread('D:/python_cv-ex/ex01/lena.jpg',cv2.IMREAD_GRAYSCALE)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow("Image", thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()