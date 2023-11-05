import socket
from tkinter import *
import tkinter as tk
from  threading import Thread
import platform
from PIL import ImageTk, Image
from tkinter import filedialog

PORT  = 8050
IP_ADDRESS = "127.0.0.1"
SERVER = None
BUFFER_SIZE = 4096

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()
setup()

def musicWindow():
    window = Tk()
    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg = 'LightSkyBlue')


    selectLabel = Label(window, text = "Select Song", bg = "LightSkyBlue", font = ("Calibri", 8))
    selectLabel.place(x = 2,  y = 1)

    listbox = Listbox(window , height = 10, width = 39, sctivestyle = 'dotbox', bg = 'LightSkyBlue', borderwidth = 2 , font = ("Calibri" , 10))
    listbox.place(x = 10 , y = 10 )

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)
 
    playButton = Button(window , text = "play" , width = 10, bd = 1 , bg = 'SkyBlue' , font = ("Calibri",10))
    playButton.place(x = 30, y = 200)

    stop= Button(window, text = "Stop", bd  =1, width = 10 , bg = "SkyBlue", font = ("Calibri", 10))
    stop.place(x = 200 , y = 200)

    upload= Button(window, text = "Upload", bd  =1, width = 10 , bg = "SkyBlue", font = ("Calibri", 10))
    upload.place(x = 30 , y = 250)

    Download = Button(window, text = "Download", bd  =1, width = 10 , bg = "SkyBlue", font = ("Calibri", 10))
    Download.place(x = 200 , y = 250)

    infoLabel= Button(window, text = "", fg = "blue", font = ("Calibri", 10))
    infoLabel.place(x = 200 , y = 200)

    window.mainloop()