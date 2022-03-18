import numpy as np
import cv2  as cv
from matplotlib import pyplot as plt

def resize_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


def change_res(capture, width, height):
    capture.set(3, width)
    capture.set(4, height)

face_cascade = cv.CascadeClassifier('C:\\Users\\Kiran\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('C:\\Users\\Kiran\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\data\\haarcascade_eye.xml')

# img = cv.imread('assets/persons6.jpg')
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# faces = face_cascade.detectMultiScale(gray, 1.1, 2)


# for (x,y,w,h) in faces:
#     cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#     roi_gray = gray[y:y+h, x:x+w]
#     roi_color = img[y:y+h, x:x+w]
#     eyes = eye_cascade.detectMultiScale(roi_gray)
#     for (ex,ey,ew,eh) in eyes:
#         cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

# cv.imshow('img',img)
# cv.waitKey(0)
# cv.destroyAllWindows()

v = cv.VideoCapture(0)
# change_res(v, 840, 1057)
while True:
    isTrue, Frame = v.read()
    img = resize_frame(Frame, .7)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 2)

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0),
                         2)

    cv.imshow('img', img)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

v.release()
cv.destroyAllWindows()