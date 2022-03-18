import cv2 as cv
import numpy as np 
from numpy import dtype

# img = cv.imread("assets\pandass.jpg")
img=cv.imread("assets/lion.jpg")


img = cv.resize(img, (500, 300), interpolation=cv.INTER_CUBIC)
cv.imshow("lion original", img)
blank=np.zeros(img.shape,dtype='uint8')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray img ", gray)

blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow("blur image ",blur)

canny = cv.Canny(blur, 125, 175)
# cv.imshow(" canny img ", canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
countours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.RETR_TREE)
cv.imshow("countours img", thresh)
print("number of counters = ", len(countours))

cv.drawContours(blank,countours,-1,(0,0,255),2)
cv.imshow("countours img",blank)
cv.waitKey()