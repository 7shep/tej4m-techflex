#Welcome to Shep's TEJ4M Tech Flex! 

import tkinter as Tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import pygame as pygame
from pygame import mixer


#Functions for the Music

def chooseFile():
    print("choose a file")
    chosenFile = askopenfilename(filetypes=[("All Files"),"*."])


#GUI!

root = Tk()
root.title("Shep's Tech Flex!!")
root.geometry("485x485")
root.configure(background="#BC13FE")
root.resizable(False, False)

fileButton = Button(root, height = 100, width=100, bg="#BC13FE", text="Choose a File", command = chooseFile)
fileButton.pack()

#runs tkinter code
root.mainloop()