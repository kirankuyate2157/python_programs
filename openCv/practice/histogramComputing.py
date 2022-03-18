from turtle import color
import cv2 as cv
from cv2 import circle
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("assets\player.webp")
cv.imshow("original image", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2),
                 ((img.shape[1] // 2 + img.shape[0] // 2) // 2), 255, -1)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("masked img", masked)

# hist = cv.calcHist([gray], [0], None, [256], [0, 256])

# plt.figure()
# plt.title("image histogram")
# plt.xlabel("Bins")
# plt.ylabel("pixles")
# plt.plot(hist)
# plt.xlim([0, 256])
# plt.show()

# color np.histogram
plt.figure()
plt.title("image histogram")
plt.xlabel("Bins")
plt.ylabel("pixles")
colors = ["b", "g", "r"]
for i, col in enumerate(colors):
    hist = cv.calcHist(masked, [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()