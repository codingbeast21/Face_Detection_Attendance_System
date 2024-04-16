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
window.title("Robotic Image Processing")
window.configure(background='white')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.geometry("500x400+550+250")
window.resizable(False, False)

message = tk.Label(window, text="Robotic Image Processing" ,bg="silver"  ,fg="black"  ,width=35  ,height=2,font=('times', 20)) 
message.place(x=0, y=0)

def btn1():
    os.system('python Human_Recoginition0.py')

def btn2():
    os.system('python Color_Detection0.py')

button1 = tk.Button(window, text="Human Recognition" , command = btn1 , fg="black" , bg="silver" ,width=20 ,height=2 , activebackground = "Red" ,font=('times', 15, ' bold '))
button1.place(x=125, y=100)
button2 = tk.Button(window, text="Color Detection" , command = btn2 , fg="black" , bg="silver" ,width=20 ,height=2 , activebackground = "Red" ,font=('times', 15, ' bold '))
button2.place(x=125, y=200)
quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="black"  ,bg="silver"  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=125, y=300)
 
window.mainloop()

