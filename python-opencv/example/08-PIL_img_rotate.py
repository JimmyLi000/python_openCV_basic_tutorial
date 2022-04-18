 #---08. PIL圖片旋轉---

from PIL import Image
img = Image.open("D:/python_cv-ex/ex01/lena.jpg")
img.rotate(90).show()
