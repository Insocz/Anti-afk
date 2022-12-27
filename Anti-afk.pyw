import threading as th
import tkinter as tk
from tkinter import messagebox
import pyautogui as pag
import random
import time

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

        self.text2 = tk.Label(self.fram, text="Size (1920 1080) def=size-screen", font=("Arial","10"), background="darkgray")
        self.text2.grid(row=1, column=0, padx=5, pady=5)

        self.txb2 = tk.Entry(self.fram, font=("Arial","10"))
        self.txb2.grid(row=1, column=1)

        self.text3 = tk.Label(self.fram, text="Mouse speed (s) def=0.5", font=("Arial","10"), background="darkgray")
        self.text3.grid(row=2, column=0, padx=5)

        self.txb3 = tk.Entry(self.fram, font=("Arial","10"))
        self.txb3.grid(row=2, column=1)

        self.fram.pack()

        self.button = tk.Button(self.root, text="Start", font=("Arial","15"), padx=10, background="#7FFF00", command=self.starter)
        self.button.pack(pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
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

    def move(self):
        
        if  self.button["text"] != "Stop":

            self.error_count = 0
            self.wait_time = 5
            self.screen_x, self.screen_y = pag.size()
            self.speed = 0.5

            self.int_w = self.txb1.get()

            if len(self.int_w) == 0:
                self.wait_time = 5
            else:
                try:
                    self.wait_time = int(self.int_w)
                except ValueError:
                    if self.error_count == 0:    
                        messagebox.showerror(title="ValueError", message="ValueError-wait time")
                        self.error_count = 1
                        self.starter()
                
            self.int_xy = self.txb2.get()

            if len(self.int_xy) == 0:
                self.screen_x, self.screen_y = pag.size()
            else:
                self.split_xy = self.int_xy.split()
                try:
                    self.screen_x, self.screen_y = self.split_xy
                except ValueError:
                    if self.error_count == 0:
                        messagebox.showerror(title="ValueError", message="ValueError-size")
                        self.error_count = 1
                        self.starter()
                else:
                    try:
                        self.screen_x = int(self.screen_x)
                        self.screen_y = int(self.screen_y)
                    except ValueError:
                        if self.error_count == 0:
                            messagebox.showerror(title="ValueError", message="ValueError-size")
                            self.error_count = 1    
                            self.starter()
                            
            self.int_s = self.txb3.get()

            if len(self.int_s) == 0:
                self.speed = 0.5
            else:
                try:
                    self.speed = float(self.int_s)
                except ValueError:
                    if self.error_count == 0:
                        messagebox.showerror(title="ValueError", message="ValueError-mouse speed")
                        self.error_count = 1    
                        self.starter()

            self.position = pag.position()
            self.count = 0

            while self.d == 1:
        
                if pag.position() == self.position:
                    self.count += 1

                else:
                    self.count = 0
                    self.position = pag.position()
            
                if self.count > self.wait_time:
                    self.x = random.randint(0, self.screen_x)
                    self.y = random.randint(0, self.screen_y)
                    pag.moveTo(self.x , self.y, self.speed)
                    self.position = pag.position()

                time.sleep(1)

    def starter(self):

        self.d = 1

        self.p1 = th.Thread(name="move", target=self.move)
        self.p2 = th.Thread(name="butt", target=self.butt)

        self.p1.start()
        self.p2.start()  

    def on_close(self):

            if self.button["text"] != "Stop":
                self.root.destroy()
            else:
                self.starter()


x = Gui()



