from tkinter import Frame
import cv2 as cv

v=cv.VideoCapture(0)
while(True):
    isTrue,Frame=v.read()
    cv.imshow("shashi..",Frame)

    if cv.waitKey(20)& 0xFF==ord("d"):
        break;
v.realease()
cv.destroyAllWindows()