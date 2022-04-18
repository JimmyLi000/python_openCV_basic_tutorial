 #---17. 畫框---

import cv2
img = cv2.imread('D:/python_cv-ex/ex01/lena.jpg')
point1 = (150,100)
point2 = (200,500)
draw_frame = cv2.rectangle(img,point1,point2,(0,255,0),5)

cv2.imshow("img",draw_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()