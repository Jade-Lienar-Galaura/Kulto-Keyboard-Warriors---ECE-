#Sam was here
#Jade was here
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

  def timer(self):
        global count
        if (count == 0):
            self.d = str(self.t.get())
            h, m, s = map(int, self.d.split(":"))
            h = int(h)
            m = int(m)
            s = int(s)
            if (s < 59):
                s += 1
            elif (s == 59):
                s = 0
                if (m < 59):
                    m += 1
                elif (m == 59):
                    m = 0
                    h += 1
            if (h < 10):
                h = str(0) + str(h)
            else:
                h = str(h)
            if (m < 10):
                m = str(0) + str(m)
            else:
                m = str(m)
            if (s < 10):
                s = str(0) + str(s)
            else:
                s = str(s)
            self.d = h + ":" + m + ":" + s
            self.t.set(self.d)
            if (count == 0):
                self.root.after(1000, self.timer)

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