from unittest import result
import cv2 as cv
import mediapipe as mp
import numpy as np

v=cv.VideoCapture(0,cv.CAP_DSHOW)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils()

# pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}

while True:
    isTrue,frame=v.read()
    imgRGB=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    # if results.multi_hand_landmarks:
    #     for handLms in results.multi_hand_landmarks:
    #         # mpDraw.draw_landmarks(frame,handLms)


    cv.imshow("video",frame)
    if cv.waitKey(20)& 0xFF == ord('d'):
        break
v.realese()
cv.destroyAllWindows()

