 #---15. opencv轉換成PIL.Image讀取影像格式---

import cv2
import numpy 
from PIL import Image

img = cv2.imread("D:/python_cv-ex/ex01/lena.jpg")
cv2.imshow('opencv format',img)
image = Image.fromarray(cv2.cv2.cvtColor(img,cv2.COLOR_RGB2BGR))
image.show()
cv2.waitKey(0)
cv2.destroyAllWindows()