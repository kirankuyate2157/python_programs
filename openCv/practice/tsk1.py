import cv2 as cv
from cv2 import waitKey


def resize_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


def change_res(capture, width, height):
    capture.set(3, width)
    capture.set(4, height)


# img=cv.imread("assets/cat.jpg")
# mysize=resize_frame(img,0.20)

# cv.imshow("cats",mysize)
# waitKey(0)

v = cv.VideoCapture("D:\\programing\\python_programms\\assets\\Girl - 27092.mp4")
# change_res(v, 840, 1057)
while True:
    isTrue, img= v.read()
    # img = resize_frame(img, .7)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow("girls", img)
    if waitKey(20) & 0xFF == ord('d'):
        break

v.release()
cv.destroyAllWindows()