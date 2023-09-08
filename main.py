#Welcome to Shep's TEJ4M Tech Flex! 

import tkinter as Tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import pygame as pygame
from pygame import mixer


#Functions for the Music

def chooseFile():
    #print("choose a file")
    chosenFile = askopenfilename(filetypes=[("All Files","*")])
    print(chosenFile)
    #Destroys the window, will be used for 
    root.destroy()


    #For determining filetypes!
    if chosenFile.endswith('.wav'):
        print('mp3')
        audioFile()
    elif chosenFile.endswith('mp4'):
        print('mp4')
        videoFile()
    else:
        print('invalid file type')
        

def audioFile():
    print('hi')
    audio = Tk()
    audio.title("Shep's Audio Player")
    audio.geometry("1280x720")
    audio.configure(background="#FFFFFF")
    audio.mainloop()

def videoFile():
    video = Tk()
    video.title("Shep's Video Player")
    video.geometry("1280x720")
    video.configure(background="#FFFFFF")
    video.mainloop()



#GUI FOR CHOOSE A FILE WINDOW!

root = Tk()
root.title("Shep's Tech Flex!!")
root.geometry("485x485")
root.configure(background="#BC13FE")
root.resizable(False, False)

fileButton = Button(root, height = 100, width=100, bg="#BC13FE", text="Choose a File", command = chooseFile)
fileButton.pack()

#runs tkinter code
root.mainloop()