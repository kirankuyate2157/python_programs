# import cv2
# import HandTrackingModule as htm
# import cvzone
# import os
# cap = cv2.VideoCapture(1)
# cap.set(3,640)
# cap.set(4,480)
# detector = htm.handDetector()
# # image1 = cv2.imread('JpgIm/2.jpg')
# # image1 = cv2.imread('PNGim/1.png',cv2.IMREAD_UNCHANGED)
# # cx,cy = 10,10
#
#
# class DragImg():
#     def __init__(self, path, posOrigin, imgType):
#
#         self.posOrigin = posOrigin
#         self.imgType = imgType
#         self.path = path
#
#         if self.imgType == 'png':
#             self.img = cv2.imread(self.path, cv2.IMREAD_UNCHANGED)
#         else:
#             self.img = cv2.imread(self.path)
#
#         # self.img = cv2.resize(self.img, (0,0),None,0.4,0.4)
#
#         self.size = self.img.shape[:2]
#
#     def update(self, cursor):
#         cx, cy = self.posOrigin
#         h, w = self.size
#
#         # Check if in region
#         if cx < cursor[0] < cx + w and cy < cursor[1] < cy + h:
#             self.posOrigin = cursor[1] - w // 2, cursor[2] - h // 2
#
# path = "photosMix"
# myList = os.listdir(path)
# print(myList)
# listImg = []
# for x, pathImg in enumerate(myList):
#     if 'png' in pathImg:
#         imgType = 'png'
#     else:
#         imgType = 'jpg'
#     listImg.append(DragImg(f'{path}/{pathImg}', [20 + x * 100, 50], imgType))
#
# print(listImg)
#
# while True:
#     success, img=cap.read()
#     img = cv2.flip(img,1)
#     img = detector.findHands(img)
#     lmList, _ = detector.findPosition(img,draw=False)
#
#     # img[cy:cy+h , cx:cx+w] = image1
#
#     if lmList:
#         l, _, _ = detector.findDis(8, 12, img,draw=False)
#         # print(l)
#         if l < 30:
#             cursor = lmList[8]
#             for imgObject in listImg:
#                 imgObject.update(cursor)
#                 # colorR = (0, 255, 0)
#                 # cx, cy = cursor[1], cursor[2]
#
#     try:
#         for imgObject in listImg:
#
#             # Draw for JPG image
#             h, w = imgObject.size
#             cx, cy = imgObject.posOrigin
#             if imgObject.imgType == "png":
#                 # Draw for PNG Images
#                 img = cvzone.overlayPNG(img, imgObject.img, [cx, cy])
#             else:
#                 img[cy:cy + h, cx:cx + w] = imgObject.img
#
#     except:
#         pass
#
#     cv2.imshow("vid", img)
#     cv2.waitKey(1)


import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import os

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)


class DragImg():
    def __init__(self, path, posOrigin, imgType):

        self.posOrigin = posOrigin
        self.imgType = imgType
        self.path = path

        if self.imgType == 'png':
            self.img = cv2.imread(self.path, cv2.IMREAD_UNCHANGED)
        else:
            self.img = cv2.imread(self.path)

        # self.img = cv2.resize(self.img, (0,0),None,0.4,0.4)

        self.size = self.img.shape[:2]

    def update(self, cursor):
        ox, oy = self.posOrigin
        h, w = self.size

        # Check if in region
        if ox < cursor[0] < ox + w and oy < cursor[1] < oy + h:
            self.posOrigin = cursor[0] - w // 2, cursor[1] - h // 2


path = "PNGim"
myList = os.listdir(path)
print(myList)

listImg = []
for x, pathImg in enumerate(myList):
    if 'png' in pathImg:
        imgType = 'png'
    else:
        imgType = 'jpg'
    listImg.append(DragImg(f'{path}/{pathImg}', [50 + x * 100, 50], imgType))

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        lmList = hands[0]['lmList']
        # Check if clicked
        length, info, img = detector.findDistance(lmList[8], lmList[12], img)
        print(length)
        if length < 60:
            cursor = lmList[8]
            for imgObject in listImg:
                imgObject.update(cursor)

    try:

        for imgObject in listImg:

            # Draw for JPG image
            h, w = imgObject.size
            ox, oy = imgObject.posOrigin
            if imgObject.imgType == "png":
                # Draw for PNG Images
                img = cvzone.overlayPNG(img, imgObject.img, [ox, oy])
            else:
                img[oy:oy + h, ox:ox + w] = imgObject.img

    except:
        pass

    cv2.imshow("Image", img)
    cv2.waitKey(1)