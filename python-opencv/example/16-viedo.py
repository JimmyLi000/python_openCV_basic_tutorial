 #---16. 讀取影片---

import cv2
import numpy 
from PIL import Image

image = Image.open("D:/python_cv-ex/ex01/lena.jpg")
image.show()
img = cv2.cvtColor(numpy.asarray(image), cv2.COLOR_RGB2BGR)

cv2.imshow('PIL.Image_format_opencv',img)
cv2.waitKey(0)
cv2.destroyAllWindows()