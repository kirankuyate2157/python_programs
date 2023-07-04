import cv2
import cvzone
import HandTrackingModule as htm
from time import sleep
from pynput.keyboard import Controller
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]
finalText = ""

keyboard = Controller()

def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]),20, rt=0,colorC=(51,255,255))
        cv2.rectangle(img, button.pos, (x + w, y + h), (127, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x+20,y+60),cv2.FONT_HERSHEY_PLAIN, 4, (229, 204, 255), 4)
    return img

class Button():
    def __init__(self,pos,text,size=[85,85]):
        self.pos = pos
        self.text = text
        self.size = size
buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

while True:
    success, img = cap.read()
    img = cv2.resize(img,(1280,720))
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList,bbox = detector.findPosition(img)

    img = drawAll(img,buttonList)

    if lmList:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size
            if x < lmList[8][1] < x + w and y<lmList[8][2]<y+h:
                cv2.rectangle(img, button.pos, (x + w, y + h), (51, 153, 255), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 60), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                l, _, _ = detector.findDis(8, 12, img, draw=True)
                print(l)

                ## when clicked
                if l < 50:
                    keyboard.press(button.text)
                    cv2.rectangle(img, button.pos, (x + w, y + h), (0, 0, 255), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 60), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                    finalText += button.text
                    sleep(0.15)
    cv2.rectangle(img, (50, 350), (700, 450), (51, 153, 255), cv2.FILLED)
    cv2.putText(img, finalText, (60, 430),cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
    cv2.imshow("vid", img)
    cv2.waitKey(1)

