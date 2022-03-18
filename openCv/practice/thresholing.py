from cv2 import threshold, waitKey
import numpy as np
import cv2 as cv

img = cv.imread("assets/images.jpg")
cv.imshow("original img", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray img",gray)

# simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("simple thresholing..", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("simple thresh_inv", thresh_inv)

# Adaptive thresholing
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,101,3)
cv.imshow("adaptive thresholding ",adaptive_thresh)

waitKey(0)