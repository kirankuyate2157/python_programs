import cv2
import numpy as np
plateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
cap = cv2.VideoCapture(0)
count=0
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success, img=cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = plateCascade.detectMultiScale(imgGray, 1.1, 5)
    for (x, y, w, h) in faces:
        area = w*h
        if area > 500:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
            cv2.putText(img,"Number Plate",(x-5,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(80,0,80),2)
            imgRe = img[y:y+h,x:x+w]
            cv2.imshow("res",imgRe)
    cv2.imshow("video",img)
    if cv2.waitKey(100) & 0xFF == ord('s'):
        cv2.imwrite("Resources/Scanned/No_plate_"+str(count)+".jpg",imgRe)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scanned saved",(150,265),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(100,30,56),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count+=1
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

