#Sam was here
#Jade was here
#Grezel was here
#Omar was here
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
    def reset(self):
                global count
                count = 1
                #set the watch to '00:00:00' 
                self.t.set('00:00:00')

    def start(self):
                global count
                count = 0
                self.timer

    def stop(self):
                global count
                count = 1

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

    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=680, height=300)
        self.canvas.pack(fill="both", expand=True)
        self.root.title("Stop Watch")
        self.root.geometry("1280x720")
        self.root.minsize(1280, 720)
        self.root.maxsize(1280, 720)
        self.t = StringVar()
        self.t.set("00:00:00")
        self.lb = Label(self.root, textvariable=self.t, font=("Times 40 bold"), bg="white")
        self.img1 = PhotoImage(file = 'Buttons\\Start.png')
        self.img2 = PhotoImage(file = 'Buttons\\Stop.png')
        self.img3 = PhotoImage(file = 'Buttons\\Reset.png')
        self.img4 = PhotoImage(file = 'Buttons\\Exit.png')
        self.img5 = PhotoImage(file = 'Buttons\\Lap.png')
        self.img6 = PhotoImage(file = 'Buttons\\Background.png')
        self.bt1 = Button(self.root, image = self.img1, command=self.start)
        self.bt2 = Button(self.root, image = self.img2, command=self.stop)
        self.bt3 = Button(self.root, image = self.img3, command=self.reset)
        self.bt4 = Button(self.root, image = self.img4, command=self.close)
        self.bt5 = Button(self.root, image = self.img5, command=self.lap)
        self.bt6 = Button(self.root, image = self.img6, command=self.image_path)

        button1_window = self.canvas.create_window(630, 150, anchor="nw", window=self.bt1)
        button2_window = self.canvas.create_window(730, 150, anchor="nw", window=self.bt2)
        button3_window = self.canvas.create_window(830, 150, anchor="nw", window=self.bt3)
        button4_window = self.canvas.create_window(930, 150, anchor="nw", window=self.bt4)
        button5_window = self.canvas.create_window(1030, 150, anchor="nw", window=self.bt5)
        button6_window = self.canvas.create_window(1130, 150, anchor="nw", window=self.bt6)
        buttonlb_window = self.canvas.create_window(960, 20, window=self.lb)

        self.scrollbar = Scrollbar(self.root, orient=VERTICAL)
        self.lapbox = Listbox(self.root,selectmode=EXTENDED, height = 5,
                         yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.lapbox.yview)
        #self.scrollbar.pack(side=RIGHT, fill=Y)
        button1_window = self.canvas.create_window(90, 250, anchor="nw", window=self.bt1)
        button2_window = self.canvas.create_window(290, 250, anchor="nw", window=self.bt2)
        button3_window = self.canvas.create_window(490, 250, anchor="nw", window=self.bt3)
        button4_window = self.canvas.create_window(690, 250, anchor="nw", window=self.bt4)
        button5_window = self.canvas.create_window(890, 250, anchor="nw", window=self.bt5)
        button6_window = self.canvas.create_window(1090, 250, anchor="nw", window=self.bt6)
        buttonlb_window = self.canvas.create_window(640, 20, window=self.lb)
        lapbox_window = self.canvas.create_window(640, 120, window=self.lapbox)
        self.label = Label(self.root, text="", font=("Times 40 bold"))

        #self.label = Label(self.root, text="", font=("Times 40 bold"))

        self.root.mainloop()


a = stopwatch()
