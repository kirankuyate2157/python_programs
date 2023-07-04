import cvzone
import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
import faceMeshModule as fm
cap = cv2.VideoCapture("D:\\programing\\python_programms\\openCv\\assets\\Girl - 27092.mp4")
detector = fm.FaceMeshDetector(maxFaces=2)
ploty = LivePlot(640,360,[20,50],invert=True)

idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]
ratioList = []
blinkCounter = 0
counter = 0
color = (255, 0, 255)

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success,img = cap.read()

    img = cv2.resize(img,(640,360))
    img,faces = detector.findFaceMesh(img)
    if faces:
        face = faces[0]
        for id in idList:
            cv2.circle(img,face[id][1:],3,color,cv2.FILLED)
        leftUp = face[159][1:]
        leftDown = face[23][1:]
        leftLeft = face[130][1:]
        leftRight = face[243][1:]
        lenghtVer, _ = detector.findDistance(leftUp, leftDown)
        lenghtHor, _ = detector.findDistance(leftLeft, leftRight)
        cv2.line(img, leftUp, leftDown, (0, 200, 0), 3)
        cv2.line(img, leftLeft, leftRight, (0, 200, 0), 3)

        ratio = int((lenghtVer / lenghtHor) * 100)
        ratioList.append(ratio)
        if len(ratioList) > 3:
            ratioList.pop(0)
        ratioAvg = sum(ratioList) / len(ratioList)
        if ratioAvg < 28 and counter == 0:
            blinkCounter += 1
            color = (0, 200, 0)
            counter = 1
        if counter != 0:
            counter += 1
            if counter > 10:
                counter = 0
                color = (255, 0, 255)
        cvzone.putTextRect(img, f'Blink Count: {blinkCounter}', (20, 50),colorR=color)
        imgPlot = ploty.update(ratioAvg)

        # cv2.imshow("Img Plot", imgPlot)
        imgS= cvzone.stackImages([img,imgPlot],1,1)
        cv2.imshow("Img stack", imgS)
    else:
        cv2.imshow("img",img)


    # cv2.imshow("vid",img)

    cv2.waitKey(25)