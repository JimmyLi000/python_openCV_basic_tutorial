 #---05灰階、模糊、邊緣偵測---

import cv2
import numpy as np

image = cv2.imread('D:/python_cv-ex/ex01/lena.jpg')    #讀取原圖

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)         #灰階

blurred = cv2.GaussianBlur(gray, (5, 5), 0)            #模糊

edges = cv2.Canny(blurred, 30, 150)                    #邊緣偵測

result = np.hstack([gray, blurred, edges])             #結果

cv2.imshow("image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
