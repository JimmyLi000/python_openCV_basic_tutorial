 #---12. 上下左右翻轉---

import cv2
img = cv2.imread('D:/python_cv-ex/ex01/lena.jpg')
cv2.imshow("before",img)

flippedimg1 = cv2.flip(img,1)     #橫向翻轉       
flippedimg2 = cv2.flip(img,0)     #縱向翻轉  
flippedimg3 = cv2.flip(img,-1)    #橫向縱向同時翻轉  

cv2.imshow("after",flippedimg1)

cv2.waitKey(0)
cv2.destroyAllWindows()
