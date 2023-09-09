#Welcome to Shep's TEJ4M Tech Flex! 

import tkinter as Tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkVideoPlayer import TkinterVideo
import pygame as pygame
from pygame import mixer
import os


#Functions for the Music

def chooseFile():
    #print("choose a file")
    chosenFile = askopenfilename(filetypes=[("All Files","*")])
    #print(chosenFile)
    #Destroys the window, will be used for 

    #For determining filetypes!
    if chosenFile.endswith('.wav'):
        mixer.init()
        root.destroy()
        #print('mp3') <-- Debug line
        audioFile(chosenFile)
    elif chosenFile.endswith('mp4'):
        root.destroy()
        #print('mp4') <-- Debug line
        videoFile(chosenFile)
    else:
        #print('invalid file type') <-- Debug line
        messagebox.showerror("Error", "Invalid file type. Please choose a \".wav\" or \".mp4\" file")


def audioFile(chosenFile):
    #print('hi') <-- Debug line.

    #Creates window for the audio file.
    audio = Tk()
    audio.title("Shep's Audio Player")
    audio.geometry("1280x720")
    audio.configure(background="#FFFFFF")
    

    #print(chosenFile) <-- debug line.

    #Plays the MP3 file.
    sound = mixer.Sound(chosenFile)
    sound.play()
    
    #Opens the GUI.
    audio.mainloop()

def videoFile(chosenFile):

    #print('hiii) <-- Debug line.

    #Video Gui!
    video = Tk()
    video.title("Shep's Video Player")
    video.geometry("1920x1080")
    video.configure(background="#FFFFFF")

    #Plays the MP4
    videoplayer = TkinterVideo(master=video, scaled=True)
    videoplayer.load(chosenFile)
    videoplayer.pack(expand=True, fill="both")

    videoplayer.play()


    #Opens the GUI.
    video.mainloop()




#GUI FOR CHOOSE A FILE WINDOW!

root = Tk()
root.title("Shep's Tech Flex!!")
root.geometry("485x485")
root.configure(background="#BC13FE")
root.resizable(False, False)

fileButton = Button(root, height = 100, width=100, bg="#BC13FE", text="Choose a File", command = chooseFile)
fileButton.pack()

#Opens the "Choose File" Window.
root.mainloop()