import tkinter as tk
from tkinter.font import Font
import time
import threading


class view:

    running = True

    def __init__(self,IOdata):
        self.IOdata = IOdata
        

    def logRun(self):
        threading.Thread(target=self._logRun).start()

    def _logRun(self):
        self.createDisplay()   

    def animation(self):
        while self.running == True:
            self.temp['text']=format(self.IOdata.temp, '.2f')
            self.sg['text']=format(self.IOdata.sg, '.3f')
            self.r.update()
            time.sleep(1)

    def createDisplay(self):
        self.r = tk.Tk()
        fontStyle = Font(size=30)
        self.r.title("Dave's Brew")
        #self.frame = tk.Frame(self.r, width='500', height='500')
        
        tk.Label(self.r, text='Temperature  ', font=fontStyle).grid(row=0, sticky=tk.W)
        self.temp = tk.Label(self.r, font=fontStyle)
        self.temp.grid(row=0, column=1)

        tk.Label(self.r, text='SG', font=fontStyle).grid(row=1, sticky=tk.W)
        self.sg = tk.Label(self.r, font=fontStyle)
        self.sg.grid(row=1, column=1)
        
        #self.frame.pack()
        self.r.after(0, self.animation)
        self.r.mainloop()
        
