#--- 靜態人臉辨識 ---

import cv2

#載入分類器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')      

#讀取圖片
img = cv2.imread('C:/Users/Tibame_T14/Desktop/python/python_cv-ex/face/avengers.jpg')                                    

# 轉成灰階圖片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 偵測臉部
faces = face_cascade.detectMultiScale(                                           
        gray,
        scaleFactor=1.2,
        minNeighbors=3,
        minSize=(32, 32))

#顯示偵測幾張臉
print('Found {0} faces!'.format(len(faces)))                                      

#繪製人臉部份的方框    
for (x, y, w, h) in faces:
   # 0, 255, 0 = Red, Green, Blue (欄位顯示顏色)
   cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)                     



cv2.imshow("img", img)                        #輸出成果
#cv2.imwrite("test.jpg", img)                 #儲存圖片                                    
cv2.waitKey(0)                                #等待按下任一按鍵
cv2.destroyAllWindows()                       #關閉視窗