import cv2
import cvzone
import HandTrackingModule as htm
import time
import numpy as np
import autopy as ap
frameR = 100
smoothening = 7
plocX, plocY = 0, 0
clocX, clocY = 0, 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector(maxHands=1)
pTime = 0
wCam, hCam = 640, 480
wScr, hScr = ap.screen.size()
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList,bbox = detector.findPosition(img,draw=False)

    if len(lmList) != 0:
        x1,y1 = lmList[8][1:]
        x2,y2 = lmList[12][1:]
        fingers = detector.fingerUp()
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 153, 79), 2)
        # print(fingers)

        if fingers[1] == 1 and fingers[2] == 0:

            x3= np.interp(x1,(frameR, wCam - frameR),(0,wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening
            ap.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 10, (255, 153, 79), cv2.FILLED)
            plocX, plocY = clocX, clocY

        if fingers[1] == 1 and fingers[2] == 1:
            l,img,_ = detector.findDis(8,12,img,draw=False)
            print(l)
            if l<30:
                cv2.circle(img, ((x1+x2)//2, (y1+y2)//2), 10, (186, 66, 45), cv2.FILLED)
                ap.mouse.click()


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,(255, 153, 79), 3)
    cv2.imshow("vid", img)
    cv2.waitKey(1)