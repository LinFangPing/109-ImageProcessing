import cv2
import numpy as np

img = cv2.imread("./image.jpg", 0)



x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)
absX = cv2.convertScaleAbs(x)# 轉回uint8
absY = cv2.convertScaleAbs(y)

dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

#cv2.imshow("orign", img)
#cv2.imshow("absX", absX)
#cv2.imshow("absY", absY)
#cv2.imshow("Result", dst)
cv2.imwrite("absX.jpg",absX)
cv2.imwrite("absY.jpg",absY)
cv2.imwrite("Result.jpg",dst)
while True :
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()