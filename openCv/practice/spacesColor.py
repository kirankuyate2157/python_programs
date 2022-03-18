from ctypes.wintypes import RGB
import cv2 as cv
from cv2 import imshow
import matplotlib.pyplot as plt

img=cv.imread("assets/nature.jpg")
cv.imshow("original img ",img)

# BGR to RGB
# rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv,imshow("rgb img",rgb)

# plt.imshow(img) #BGR TO RGB
# plt.show()

# BGR to Grayscale img
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gary img",gray)

# BGR to HSV 
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv img ",hsv)

# BGR to L_A_B
# lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow("LAB img ",lab)

#  HSV to BGR 
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow("Hsv_BGR",hsv_bgr)

cv.waitKey(0)
