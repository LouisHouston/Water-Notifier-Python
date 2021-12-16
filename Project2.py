import tkinter as tk
from tkinter import ttk
from tkinter.constants import FALSE
from plyer import notification
import time
from PIL import Image
from pystray import MenuItem as item
import pystray
import datetime
#img = PhotoImage(file="C:\\Users\\Louis\\Dropbox\\PythonProjects\\Project2\\water.ico")


intervals = (
    ("30m" , 30 ),
    ("1hr" , 60 ),
    ("1hr 30m " , 90 ),
    ("2hr" , 120 ) 
    )

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # root window
        self.title('Gatz Notifier')
        self.geometry('225x250')
        self.resizable(False, False)
        self.style = ttk.Style(self)
        self.iconbitmap('C:\\Users\\Louis\\Dropbox\\PythonProjects\\Project2\\water.ico')
        self.time = 0
        
        def changeinterval():
            while(True):
                notification.notify(
                    title = "Water Notifier" ,

                    message = "Drink drink drink some water!",

                    app_icon = 'C:\\Users\\Louis\\Dropbox\\PythonProjects\\Project2\\water.ico',

                    timeout = 15
                )
                


        # label
        label = ttk.Label(self, text='Water Notification')
        label.grid(column=0, row=0, padx=10, pady=10,  sticky='w')

        label = ttk.Label(self, text = "Intervals")
        label.grid(column = 0 , row = 1, padx = 10, sticky = 'w')

        
        # button
        btn = ttk.Button(self, text='Activate', command = changeinterval)
        btn.grid(column=1, row=0, padx=10, pady=10,  sticky='w')


        # radio button
        self.selected_time = tk.StringVar()
        theme_frame = ttk.LabelFrame(self, text='Intervals')
        theme_frame.grid(padx = 5, column=0, row=0, sticky='w')

        for durations in intervals:
            r = ttk.Radiobutton(
                self,
                text=durations[0],
                value = durations[1],
                variable = self.selected_time,)
            r.grid(padx = 15,sticky = "w")

    def change_theme(self):
        self.style.theme_use(self.selected_theme.get())

if __name__ == "__main__":
    app = App()
    #app.after(15000, app.changeinterval())
    app.mainloop()