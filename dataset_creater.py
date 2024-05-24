# import packages

import cv2 #opencv camera
import numpy as np #numpy array
import sqlite3 #sqlite is database

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # to detect the faces in camera
cam = cv2.VideoCapture(0)  # 0 is used for web camera

def inserttoupdate(Id, Name, Age):          # Function is for sqlite database
    conn = sqlite3.connect("sqlite.db")   # connect
    cmd = "SELECT * FROM STUDENTS WHERE ID="+str(Id)
    cursor = conn.execute(cmd)          # cursor to execute this command
    isRecordExist = 0                   # assume there is no record in our table
    for row in cursor:
        isRecordExist = 1
    if(isRecordExist==1):               # if there is a record exist in our table
        conn.execute("UPDATE STUDENTS SET NAME=? WHERE ID=?", (Name, Id))
        conn.execute("UPDATE STUDENTS SET Age=? WHERE ID=?", (Age, Id))
    else:                               # If the record doesnot exist we insert the values
        conn.execute("INSERT INTO STUDENTS (Id, Name, Age) values (?, ?, ?)", (Id, Name, Age))
    conn.commit()
    conn.close()

# insert user defined values into table
Id = input("Enter User Id")
Name = input("Enter User Name")
Age = input("Enter User Age")

inserttoupdate(Id, Name, Age)

#detect face in web camera coding

sampleNum = 0       # assume that there is no samples in dataset
while(True):
    ret, img = cam.read() # We are going to open camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Image covert into gray
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)  # scaling factor auto change in pycharm IDE
    for(x, y, w, h) in faces:
        sampleNum = sampleNum+1  # If face is dedected increments
        cv2.imwrite("datasets/user."+str(Id)+"."+str(sampleNum)+".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
        cv2.waitKey(100)   # delay time
    cv2.imshow("Face", img)   # show faces detected in web camera
    cv2.waitKey(1)
    if(sampleNum>20): # if the dataset is > 20 break
        break
cam.release()
cv2.destroyAllWindows()   # quit










