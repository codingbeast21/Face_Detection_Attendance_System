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
window.title("Color Detection")
window.configure(background='white')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.geometry("500x400+550+250")
window.resizable(False, False)

message = tk.Label(window, text="Color Detection" ,bg="silver"  ,fg="black"  ,width=35  ,height=2,font=('times', 20)) 
message.place(x=0, y=0)

lbl = tk.Label(window, text="Enter Command",width=15  ,height=2  ,fg="black"  ,bg="silver" ,font=('times', 10, ' bold ') ) 
lbl.place(x=35, y=150)

txt = tk.Entry(window,width=40 ,bg="silver" ,fg="black",font=('times', 10, ' bold '))
txt.place(x=185, y=157)

def sub():
    os.system(txt.get())

submitButton = tk.Button(window, text="Submit", command=sub  ,fg="black"  ,bg="silver"  ,width=10  ,height=2 ,activebackground = "Red" ,font=('times', 10, ' bold '))
submitButton.place(x=150, y=250)
quitWindow = tk.Button(window, text="Quit/Back", command=window.destroy  ,fg="black"  ,bg="silver"  ,width=10  ,height=2, activebackground = "Red" ,font=('times', 10, ' bold '))
quitWindow.place(x=300, y=250)
 
window.mainloop()
