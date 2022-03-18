import cv2 as cv
from cv2 import waitKey
import numpy as np

img = cv.imread("assets\player.webp")
cv.imshow("original image", img)
average = cv.blur(img, (3, 3))
cv.imshow("average image blur", average)

guss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow("guss img blur", guss)

median = cv.medianBlur(img, 3)
cv.imshow("median img blur", median)

bilateral = cv.bilateralFilter(img, 3, 15, 15)
cv.imshow("bilateral image blur", bilateral)
waitKey(0)