from turtle import back
import cv2 as cv
from cv2 import rectangle
from cv2 import circle
from cv2 import waitKey
from cv2 import bitwise_and
from cv2 import bitwise_or
from cv2 import bitwise_xor
from cv2 import bitwise_not
import numpy as np

blank = np.zeros((500, 500), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (50, 50), (450, 450), 255, -1)
circle = cv.circle(blank.copy(), (250, 250), 250, 255, -1)

# cv.imshow("rectangle", rectangle)
# cv.imshow("circle ", circle)

bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow("bitwiswe_and",bitwise_and)

bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow("bitwise_or",bitwise_or)

bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow("bitwise_xor",bitwise_xor)

bitwise_not=cv.bitwise_not(rectangle,circle)
cv.imshow("bitwise_not",bitwise_not)



waitKey(0)
