from cv2 import Laplacian, threshold, waitKey
import numpy as np
import cv2 as cv

img = cv.imread("assets/images.jpg")
cv.imshow("original img", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray img", gray)

# Laplacian img
# lap = cv.Laplacian(gray, cv.CV_64F)
# lap = np.uint8(np.absolute(lap))
# cv.imshow("laplacian img", lap)

# sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow("sobelx", sobelx)
cv.imshow("sobely", sobely)
cv.imshow("combined Sobel", combined_sobel)

canny=cv.Canny(gray,150,255)
cv.imshow("canny img",canny)

cv.waitKey(0)
