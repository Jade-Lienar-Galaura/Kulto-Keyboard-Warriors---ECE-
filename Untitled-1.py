# im in - jade
# im in - labos
# hello
# i am in - omar
# i'm in - calvin
# Wassup mga idols - Sam edgys
#lamaw
# gay
import imp
from tkinter import *
import sys
import time
global count
from tkinter import filedialog
from PIL import ImageTk, Image
count = 0


class stopwatch():
    def reset(self):
        global count
        count = 1
        self.t.set('00:00:00')

    def start(self):
        global count
        count = 0
        self.timer()

    def stop(self):
        global count
        count = 1

    def close(self):
        self.root.destroy()

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

    def lap(self):
        h, m, s = map(int, self.d.split(":"))
        h = str(h).zfill(2)
        m = str(m).zfill(2)
        s = str(s).zfill(2)
        lp = (f"{h}:{m}:{s}")
        self.lbl = StringVar()
        self.lbl.set(f"{lp}")
        self.lapbox.insert(END, (f"{h}:{m}:{s}"), 0,0)
        self.lapbox.yview_moveto(1)


    def image_path(self):
        photoloc = filedialog.askopenfilename()
        img = Image.open(photoloc)
        resize =img.resize((1280, 720), Image.ANTIALIAS)
        bg = ImageTk.PhotoImage(resize)
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.back = Label(root, image=bg)
        self.back.pack(padx=0, pady=0)


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
        self.lb = Label(self.root, textvariable=self.t, font=("Times" , 40 , "bold"), bg="white")
        self.bt1 = Button(self.root, text="Start", command=self.start, font=("Times" , 12 , "bold"), bg=("green"))
        self.bt2 = Button(self.root, text="Stop", command=self.stop, font=("Times" , 12 , "bold"), bg=("red"))
        self.bt3 = Button(self.root, text="Reset", command=self.reset, font=("Times" , 12 , "bold"), bg=("orange"))
        self.bt4 = Button(self.root, text="Exit", command=self.close, font=("Times" , 12 , "bold"), bg=("yellow"))
        self.bt5 = Button(self.root, text="Lap", command=self.lap, font=("Times" , 12 , "bold"), bg=("blue"))
        self.bt6 = Button(self.root, text="Change background", command=self.image_path, font=("Times", 12 , "bold"),
                          bg=("pink"))

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
        
        button1_window = self.canvas.create_window(310, 250, anchor="nw", window=self.bt1)
        button2_window = self.canvas.create_window(410, 250, anchor="nw", window=self.bt2)
        button3_window = self.canvas.create_window(510, 250, anchor="nw", window=self.bt3)
        button4_window = self.canvas.create_window(610, 250, anchor="nw", window=self.bt4)
        button5_window = self.canvas.create_window(710, 250, anchor="nw", window=self.bt5)
        button6_window = self.canvas.create_window(810, 250, anchor="nw", window=self.bt6)
        buttonlb_window = self.canvas.create_window(640, 20, window=self.lb)
        lapbox_window = self.canvas.create_window(640, 120, window=self.lapbox)
        self.label = Label(self.root, text="", font=("Times 40 bold"))

        #self.label = Label(self.root, text="", font=("Times 40 bold"))

        self.root.mainloop()


a = stopwatch()
