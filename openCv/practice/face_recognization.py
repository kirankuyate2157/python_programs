from operator import truediv
import numpy as np
import os
import cv2 as cv

people = []
DIR = r"D:\\programing\\python_programms\\openCv\\assets\\peopleData"
names = os.listdir(DIR)
face_cascade = cv.CascadeClassifier(
    'C:\\Users\\Kiran\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml'
)
for k in names:
    people.append(k)
print(people)

features = np.load("D:\\programing\\python_programms\\openCv\\practice\\features.npy",allow_pickle=True)
Labels = np.load("D:\\programing\\python_programms\\openCv\\practice\\labels.npy")
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("D:\\programing\\python_programms\\openCv\\practice\\face_trained.yml")

img = cv.imread(r"C:\\Users\\Kiran\\Pictures\\Saved Pictures\\imagestyrywd.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("unidentified person", gray)

face_rect = face_cascade.detectMultiScale(gray, 1.1, 2)
for (x, y, w, h) in face_rect:
    faces_roi = gray[y:y + h, x:x + w]
    label, confidance = face_recognizer.predict(faces_roi)
    print(f"label = {people[label]} ,with the confidace {confidance}")

    cv.putText(img,people[label],(x+20,y-7),cv.FONT_HERSHEY_COMPLEX_SMALL,0.5,(0,0,220),thickness=1)
    cv.rectangle(img,(x,y),(x+h,y+w),(0,255,0),thickness=4)
cv.imshow("detected image ",img)
cv.waitKey(0)