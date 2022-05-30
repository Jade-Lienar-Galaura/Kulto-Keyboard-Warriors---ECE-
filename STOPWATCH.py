#Sam was here
#Jade was here
#Omar was here
#Calvin was here
#Grezel was here
# Thanks for the cooperation guys! Really appreciate na ginawa niyo ang parts niyo agad <3 much loves! - Sam
import imp
from tkinter import *
import sys
import time
global count
from tkinter import filedialog
from PIL import ImageTk, Image
import pygame
from pygame import mixer


pygame.init()


#mixer.music.load() - SONG HERE !!!!!!!!!!!!!!!!!
#Jade: i will upload na the music 
mixer.music.load('Avicii - Broken Arrows (Instrumental).wav')
mixer.music.set_volume(1)
mixer.music.play(-1)

count = 0

class stopwatch():
    #LABOS - START/STOP FUNCTION
    def reset(self):
        global count
        count = 1
        #set the watch to '00:00:00' 
        self.t.set('00:00:00')

    def start(self):
        global count
        count = 0
        self.timer()
                #else:
                #count = 1
                #self.timer()

    def stop(self):
        global count
        count = 1

    def close(self):
        self.root.destroy()


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
    def lap(self):
        h, m, s = map(int, self.d.split(":"))
        h = str(h).zfill(2)
        m = str(m).zfill(2)
        s = str(s).zfill(2)
        lp = (f"{h}:{m}:{s}")
        self.lbl = StringVar()
        self.lbl.set(f"{lp}")
        self.lapbox.insert(END, (f"{h}:{m}:{s}"))
        self.lapbox.yview_moveto(1)
    
    
    #Sam - parts custom bg
    def image_path(self):
        photoloc = filedialog.askopenfilename()
        img = Image.open(photoloc)
        resize =img.resize((1280, 720), Image.ANTIALIAS)
        bg = ImageTk.PhotoImage(resize)
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.back = Label(root, image=bg)
        self.back.pack(padx=0, pady=0)


    #OMAR - BUTTONS/ REST OF INNIT ASIDE FROM BUTTON WINDOWS

    

a = stopwatch()


