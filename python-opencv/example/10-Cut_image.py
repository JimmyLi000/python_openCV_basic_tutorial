 #---09. 切割影像---

import cv2
img = cv2.imread('D:/python_cv-ex/ex01/lena.jpg')
point1 = (150,100)
point2 = (200,500)
crop_img = img[point1[1]:point2[1],point1[0]:point2[0]]
cv2.imshow("img", crop_img)
cv2.imwrite("crop.jpg", crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
