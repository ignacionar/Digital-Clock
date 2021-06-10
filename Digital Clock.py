import time
from tkinter import *
from tkinter import ttk
import sys
from playsound import playsound

root = Tk()

root.title("Digital Clock")
root.resizable(0, 0)
root.geometry("600x120")
root.iconbitmap("DC.ico")
root.configure(background="black")
miLabel = Label(root, text="Made by I.N. 10/06/2021", font=("Monaco", 8, "bold"), bg="black", fg="green2").place(x=215, y=95)


def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)

clock = Label(root, font=("DS-Digital",66),bg="black",fg="green2")
clock.pack()



get_time()

root.mainloop()