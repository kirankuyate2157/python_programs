from gettext import translation
from turtle import down, left, right, up
import cv2 as cv
from cv2 import INTER_CUBIC
import numpy as np

img = cv.imread("assets/dviv.jpg")
img = cv.resize(img, (500, 500), interpolation=INTER_CUBIC)
cv.imshow("original images", img)


# translation
def translate(src, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimension = (src.shape[0], src.shape[1])
    return cv.warpAffine(src, transMat, dimension)


# -x ->left
# -y ->up
#  x ->right
#  y ->down
# translated = translate(img, -100, 10)
# cv.imshow("translated image", translated)

# image rotation 
def rotate(src, angle, rotpoint=None):
    (height, width) = src.shape[0:2]
    if rotpoint is None:
        rotpoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimension = (width, height)

    return cv.warpAffine(src, rotMat, dimension)

# rotImg = rotate(img, 45)
# cv.imshow("roterted image ", rotImg)
# rotImg = rotate(rotImg, 85)
# cv.imshow("roterted image2 ", rotImg)

# resize image
# resize=cv.resize(img,(500,500),interpolation=INTER_CUBIC)
# cv.imshow("resized image",resize)

# fliping image 
# flip=cv.flip(img,-1)
# cv.imshow("fliped img ",flip)

# croping image 
croped=img[100:360,100:378]
cv.imshow("croped img ",croped)

cv.waitKey(0)