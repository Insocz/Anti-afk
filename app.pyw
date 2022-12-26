
import tkinter as tk
import pyautogui as pag
import random
import time
import os
import subprocess
import threading as th

class Gui:
    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Anti-Afk")
        self.root.geometry("500x300")

        self.fram = tk.Frame(self.root, background="darkgray", padx=10, pady=10)
        self.fram.columnconfigure(0, weight=1)
        self.fram.rowconfigure(0, weight=1)
        self.fram.columnconfigure(1, weight=1)
        self.fram.rowconfigure(1, weight=1)
        self.fram.columnconfigure(2, weight=1)
        self.fram.rowconfigure(2, weight=1)

        self.label = tk.Label(self.root, text="Anti-Afk", font=("Arial","15"))
        self.label.pack(pady=10)

        self.text1 = tk.Label(self.fram, text="Wait time (s) def=5", font=("Arial","10"), background="darkgray")
        self.text1.grid(row=0, column=0, padx=5)

        self.txb1 = tk.Entry(self.fram, font=("Arial","10"))
        self.txb1.grid(row=0, column=1)

        self.text2 = tk.Label(self.fram, text="Size (px) def=size-screen", font=("Arial","10"), background="darkgray")
        self.text2.grid(row=1, column=0, padx=5, pady=5)

        self.txb2 = tk.Entry(self.fram, font=("Arial","10"))
        self.txb2.grid(row=1, column=1)

        self.text3 = tk.Label(self.fram, text="Mouse speed (s) def=2", font=("Arial","10"), background="darkgray")
        self.text3.grid(row=2, column=0, padx=5)

        self.txb3 = tk.Entry(self.fram, font=("Arial","10"))
        self.txb3.grid(row=2, column=1)

        self.fram.pack()

        self.button = tk.Button(self.root, text="Start", font=("Arial","15"), padx=10, background="#7FFF00", command=self.starter)
        self.button.pack(pady=10)

        self.root.mainloop()
        
    def butt(self):

        if self.button["background"] != "#7FFF00":
            self.button["background"] = "#7FFF00"
            self.button["text"] = "Start"
            self.d = 0

        elif self.button["background"] != "#ff4122":
            self.button["background"] = "#ff4122"
            self.button["text"] = "Stop"
            self.d = 1

    def pron(self):
        while self.d == 1:
            print("hi")
            time.sleep(1)

    def move(self):
        self.position = pag.position()
        self.count = 0
        self.screen_x, self.screen_y = pag.size()

        while self.d == 1:
        
            if pag.position() == self.position:
                self.count += 1

            else:
                self.count = 0
                self.position = pag.position()
            
            if self.count > 5:
                self.x = random.randint(0, self.screen_x)
                self.y = random.randint(0, self.screen_y)
                pag.moveTo(self.x , self.y, 0.5)
                self.position = pag.position()

            print(self.count)
            time.sleep(1)

    def starter(self):

        self.d = 1

        self.p1 = th.Thread(name="move", target=self.move)
        self.p2 = th.Thread(name="butt", target=self.butt)

        self.p1.start()
        self.p2.start()  


x = Gui()



