import cv2
import numpy as np
from skimage.feature import local_binary_pattern
from scipy import ndimage
from matplotlib import pyplot as plt
def marker(img):
    images = cv2.imread(img)
    kernel = np.ones((3,3), np.uint8)
    gray = cv2.cvtColor(images,cv2.COLOR_BGR2GRAY)
    ret,markerImag = cv2.threshold(gray,10,255,cv2.THRESH_BINARY_INV)
    markerImag = cv2.dilate(markerImag, kernel, iterations = 4)
    markerImag = cv2.erode(markerImag, kernel, iterations = 5)
    #cv2.imshow("marker",markerImag)
    cv2.imwrite("marker.jpg",markerImag)
    ret, markers = cv2.connectedComponents(markerImag) #markerImag > 0 : marker  | |  markerImag == 0 : ignore
    return markers
    
markers = marker("marker_img.jpg")
image = cv2.imread("original.jpg")
Hist = cv2.calcHist([image], [0], None, [256], [0,256])
plt.plot(Hist)
plt.show()
result = cv2.watershed(image,markers)#result == 1 : ignore  | |  result == -1 : edge
image[result==-1]=[0,255,0]
cv2.imwrite("watershed.jpg",image)
cv2.imshow('result', image)
#plt.subplot(2, 2, 2)
#plt.title('img')
#plt.imshow(image)
#plt.show()
while True :
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()