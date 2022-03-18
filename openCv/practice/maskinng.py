import cv2 as cv
from cv2 import waitKey
import numpy as np

img = cv.imread("assets/cat.jpg")
img = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("original image", img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow(" blank img", blank)
mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 200, 255, -1)
cv.imshow("mask img", mask)

# masked = cv.bitwise_and(img, img, mask=mask)
masked = cv.bitwise_or(img, img, mask=mask)
cv.imshow("masked image", masked)

waitKey(0)