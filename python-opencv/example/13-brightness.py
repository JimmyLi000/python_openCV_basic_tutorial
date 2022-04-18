 #---13. 亮度及對比調整---

import cv2
import numpy as np
img = cv2.imread('D:/python_cv-ex/ex01/lena.jpg')

result = np.uint8(np.clip((1.5 * img + 100),0,255))

cv2.imshow("img",result)
cv2.waitKey(0)
cv2.destroyAllWindows()