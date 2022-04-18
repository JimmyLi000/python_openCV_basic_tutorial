#---01讀取圖片---

import cv2

#讀取圖片的位置
img = cv2.imread('D:python_cv-ex/face/lena.jpg')

#輸出結果
cv2.imshow("img", img)

#將畫面停留                                            
cv2.waitKey(0)
#按下任意鍵則關閉所有視窗
cv2.destroyAllWindows()
