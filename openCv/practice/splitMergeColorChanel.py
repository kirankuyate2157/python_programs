import cv2 as cv
from cv2 import waitKey
from cv2 import split
from cv2 import merge
import numpy as np

img = cv.imread("assets/natur2.jpg")
cv.imshow("original image", img)
print(img.shape)
blank = np.zeros(img.shape[:2], dtype='uint8')
b, g, r = split(img)
print(b.shape)
print(g.shape)
print(r.shape)

blue = merge([b, blank, blank])
green = merge([blank, g, blank])
red = merge([blank, blank, r])
cv.imshow("red img", red)
cv.imshow("green img", green)
cv.imshow("blue img", blue)

# merge=cv.merge([b,g,r])
# cv.imshow("merged img ",merge)

waitKey(0)