import cv2
import HandTrackingModule as htm
import time
import mediapipe as mp
import numpy as np
import cvzone
cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)
detector = htm.handDetector(detectionCon=0.8)
colorR = (255,0,255)
cx,cy = 50,50
w,h = 100,100



class DragRect():
    def __init__(self, posCenter, size=[100, 100]):
        self.posCenter = posCenter
        self.size = size

    def update(self, cursor):
        cx, cy = self.posCenter[0],self.posCenter[1]
        w, h = self.size[0],self.size[1]
        if cx - w // 2 < cursor[1] < cx + w // 2 and cy - h // 2 < cursor[2] < cy + h // 2:
            self.posCenter[0] = cursor[1]
            self.posCenter[1] =cursor[2]

rectList = []
for x in range(5):
    rectList.append(DragRect([x * 100 + 5, 50]))
# rect = DragRect([50,50],[100,100])

while True:
    success, img=cap.read()
    img = cv2.flip(img,1)
    img = detector.findHands(img)
    lmList , bbox = detector.findPosition(img)
    if lmList:
        l,_,_= detector.findDis(8,12,img,draw=False)
        print(l)
        if l < 30:
            cursor = lmList[8]

            for rect in rectList:
                rect.update(cursor)

            # if cx - w // 2 < cursor[1] < cx + w // 2 and cy - h // 2 < cursor[2] < cy + h // 2:
            #     colorR = (0, 255, 0)
            #     cx, cy = cursor[1], cursor[2]
    for rect in rectList:
        cx, cy = rect.posCenter[0], rect.posCenter[1]
        w, h = rect.size[0], rect.size[1]
        # print(cx,cy,w,h)
        cv2.rectangle(img, (cx - w // 2, cy - h // 2), (cx + w // 2, cy + h // 2), colorR, cv2.FILLED)

        cvzone.cornerRect(img, (cx - w // 2, cy - h // 2, w, h), 20, rt=0)


    ##draw with transperency
    imgNew = np.zeros_like(img, np.uint8)
    for rect in rectList:
        cx, cy = rect.posCenter
        w, h = rect.size
        cv2.rectangle(imgNew, (cx - w // 2, cy - h // 2),
                      (cx + w // 2, cy + h // 2), colorR, cv2.FILLED)
        cvzone.cornerRect(imgNew, (cx - w // 2, cy - h // 2, w, h), 20, rt=0)

    out = img.copy()
    alpha = 0.1
    mask = imgNew.astype(bool)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
    cv2.imshow("vid", out)
    cv2.waitKey(1)
