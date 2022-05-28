#Sam was here

import imp
from tkinter import *
import sys
import time
global count
from tkinter import filedialog
from PIL import ImageTk, Image
count = 0

class stopwatch():

#LABOS - START/STOP FUNCTION

#JADE - CLOSE / HALF SA TIMER

#CLYDE - HALF SA TIMER / LAP'

def image_path(self):
        photoloc = filedialog.askopenfilename()
        img = Image.open(photoloc)
        resize =img.resize((1280, 720), Image.ANTIALIAS)
        bg = ImageTk.PhotoImage(resize)
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.back = Label(root, image=bg)
        self.back.pack(padx=0, pady=0)

#OMAR - BUTTONS/ REST OF INNIT ASIDE FROM BUTTON WINDOWS