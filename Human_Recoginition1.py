import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font

window = tk.Tk()
window.title("Human Recognition")
window.configure(background='white')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.geometry("500x400+550+250")
window.resizable(False, False)

message = tk.Label(window, text="Human Recoginition" ,bg="silver"  ,fg="black"  ,width=35  ,height=2,font=('times', 20)) 
message.place(x=0, y=0)

lbl = tk.Label(window, text="Id",width=15  ,height=2  ,fg="black"  ,bg="silver" ,font=('times', 10, ' bold ') ) 
lbl.place(x=35, y=110)

txt = tk.Entry(window,width=40 ,bg="silver" ,fg="black",font=('times', 10, ' bold '))
txt.place(x=185, y=117)

lbl2 = tk.Label(window, text="Name",width=15  ,fg="black"  ,bg="silver"    ,height=2 ,font=('times', 10, ' bold ')) 
lbl2.place(x=35, y=170)

txt2 = tk.Entry(window,width=40  ,bg="silver"  ,fg="black",font=('times', 10, ' bold ')  )
txt2.place(x=185, y=177)

lbl3 = tk.Label(window, text="Notifications ",width=15  ,fg="black"  ,bg="silver"  ,height=2 ,font=('times', 10, ' bold ')) 
lbl3.place(x=35, y=240)

message = tk.Label(window, text="" ,bg="silver"  ,fg="black"  ,width=40  ,height=2, activebackground = "yellow" ,font=('times', 10, ' bold ')) 
message.place(x=185, y=240)

def clear():
    txt.delete(0, 'end')
    txt2.delete(0, 'end')
    res = ""
    message.configure(text= res)
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
 
def TakeImages():        
    Id=(txt.get())
    name=(txt2.get())
    if(is_number(Id)):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)         
                sampleNum=sampleNum+1
                cv2.imwrite("TrainingImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                cv2.imshow('frame',img) 
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif sampleNum>60:
                break
        cam.release()
        cv2.destroyAllWindows() 
        res = "Images Saved for ID : " + Id +" Name : "+ name
        row = [Id , name]
        with open('Database\Database.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message.configure(text= res)
    else:
        res = "Enter Numeric Id"
        message.configure(text= res)
    
def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Image Trained"
    message.configure(text= res)

def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    faces=[]
    Ids=[]
    for imagePath in imagePaths:
        pilImage=Image.open(imagePath).convert('L')
        imageNp=np.array(pilImage,'uint8')
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids

clearButton = tk.Button(window, text="Clear All", command=clear  ,fg="black"  ,bg="silver"  ,width=10  ,height=2 ,activebackground = "Red" ,font=('times', 10, ' bold '))
clearButton.place(x=70, y=320)
takeImg = tk.Button(window, text="Take Images", command=TakeImages  ,fg="black"  ,bg="silver"  ,width=10  ,height=2, activebackground = "Red" ,font=('times', 10, ' bold '))
takeImg.place(x= 165, y=320)
trainImg = tk.Button(window, text="Train Images", command=TrainImages  ,fg="black"  ,bg="silver"  ,width=10  ,height=2, activebackground = "Red" ,font=('times', 10, ' bold '))
trainImg.place(x=260, y=320)
quitWindow = tk.Button(window, text="Quit/Back", command=window.destroy  ,fg="black"  ,bg="silver"  ,width=10  ,height=2, activebackground = "Red" ,font=('times', 10, ' bold '))
quitWindow.place(x=355, y=320)
 
window.mainloop()
