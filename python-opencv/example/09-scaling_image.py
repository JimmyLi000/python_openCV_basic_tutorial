 #---09. 圖片縮放---

import cv2
pic = cv2.imread('D:/python_cv-ex/ex01/lena.jpg')
pic = cv2.resize(pic, (200, 100), interpolation=cv2.INTER_CUBIC)
cv2.imshow('', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
