import numpy as np
import cv2 as cv
import os

people = []
DIR = r"D:\\programing\\python_programms\\openCv\\assets\\peopleData"
names = os.listdir(DIR)
face_cascade = cv.CascadeClassifier(
    'C:\\Users\\Kiran\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml'
)

for k in names:
    people.append(k)
print(people)

features = []
Labels = []


def face_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_mat = cv.imread(img_path)
            gray = cv.cvtColor(img_mat, cv.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 2)
            for (x, y, w, h) in faces:
                face_roi = gray[y:y + h, x:x + w]
                features.append(face_roi)
                Labels.append(label)


face_train()
features = np.array(features, dtype='object')
Labels = np.array(Labels)
# print(f"no of features detected = {len(features)}")
# print(f"no of Labels = {len(Labels)}")

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, Labels)
face_recognizer.save("openCv\\practice\\face_trained.yml")
np.save("openCv\\practice\\features.npy",features)
np.save("openCv\\practice\\labels.npy", Labels)

print(features)