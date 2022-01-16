#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
import sys
import os

global password
# Set password here (yes, in plain text, is that a problem?)
password = "password"


arguments = list(sys.argv)
arguments.remove(arguments[0])
if len(arguments)>1:
    if arguments[0] == "-c":
        arguments.remove("-c")
global strcmd
strcmd = str(" ".join(arguments))

def allow():
    root.destroy()
    os.system(f"echo {password} | sudo -E -S {strcmd}")

def dontallow():
    root.destroy()

def main(cmd):
    global root
    root = Tk()
    root.eval('tk::PlaceWindow . center')
    frm = ttk.Frame(root, padding=20)
    frm.grid()
    ttk.Label(frm, text=f"Command '{cmd}' is trying to run with elevated permissions").grid(column=1, row=0)
    ttk.Button(frm, text="Don't allow", command=dontallow).grid(column=0, row=1)
    ttk.Button(frm, text="Allow", command=allow).grid(column=2, row=1)
    window_height = 80
    window_width = 480 + len(strcmd)*6
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    root.title("simple-sudo")
    root.mainloop()

if __name__ == "__main__":
    main(strcmd)
