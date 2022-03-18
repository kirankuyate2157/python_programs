from typing import DefaultDict
import cv2 as cv
from cv2 import BORDER_DEFAULT
from cv2 import erode
from cv2 import INTER_AREA
from cv2 import INTER_CUBIC
from matplotlib import image
from numpy import uint16


def chang_size(src, scale=0.75):
    width = int(src.shape[0] * scale)
    height = int(src.shape[1] * scale)
    dimension = (width, height)
    return cv.resize(src, dimension, interpolation=cv.INTER_AREA)


img = cv.imread("assets\dviv.jpg")
img = chang_size(img, .1)

# blur image
# img=cv.GaussianBlur(img,(9,9),cv.BORDER_CONSTANT)
cv.imshow("original cat", img)

# gray image
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gay img", gray)

# # scaceding image
# canny = cv.Canny(img, 125, 175)
# cv.imshow("canny image", canny)

# # dilated image
# dialet = cv.dilate(img, (7, 7), iterations=6)
# cv.imshow("dialet image ", dialet)

# # eroding image
# Erode = cv.erode(img, (7, 7), iterations=7)
# cv.imshow("Eroded img", Erode)

# resize image
resize=cv.resize(img,(500,500),interpolation=INTER_CUBIC)
cv.imshow("resized image",resize)

#croping 
croped=img[100:330,100:330]
cv.imshow("croped img",croped)

# v = cv.VideoCapture("assets/Yoga - 27087.mp4")
# while True:
#     isTrue, frame = v.read()
#     fr=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#     fr=cv.GaussianBlur(frame,(9,9),cv.BORDER_CONSTANT)
#     cv.imshow("video", fr)
#     if (cv.waitKey(20) & 0xFF == ord('d')):
#         break

cv.waitKey(0)