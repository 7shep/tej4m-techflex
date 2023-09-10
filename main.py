#Welcome to Shep's TEJ4M Tech Flex! 

import tkinter as Tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkVideoPlayer import TkinterVideo
import pygame as pygame
from pygame import mixer
import keyboard
import threading
import time

#Functions for the Music

#For pausing, using the same system as my last tech flex!
num = 0

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
    icon = PhotoImage(file='./Images/icon.png')
    audio.iconphoto(False, icon)
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
    icon = PhotoImage(file='./Images/icon.png')
    video.iconphoto(False, icon)
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



#Detecting Space Key
def spaceKey():
    while True:
        if keyboard.is_pressed('space'):
            #print('Space key is pressed.') debug line
            pauseFile()
        time.sleep(0.1)

#Threading runs this code in the background, target is the function. It is looking for the "spaceKey" function to be called.
spacekeythread = threading.Thread(target=spaceKey)
#Setting daemon to true allows me to exit the program.
spacekeythread.daemon = True
#Starts the threading
spacekeythread.start()

def pauseFile():
    global num
    num += 1
    if mixer.get_busy():
        if (num%2) == 0:
            mixer.unpause()
            print('Music Unpaused')
        else:
            mixer.pause()
            print('Music paused')
    else:
        print('Music is not playing.')
    print(num)




#GUI FOR CHOOSE A FILE WINDOW!

root = Tk()
icon = PhotoImage(file='./Images/icon.png')
root.iconphoto(False, icon)
root.title("Shep's Tech Flex!!")
root.geometry("485x485")
root.configure(background="#BC13FE")
root.resizable(False, False)

fileButton = Button(root, height = 100, width=100, bg="#BC13FE", text="Choose a File", command = chooseFile)
fileButton.pack()

#Opens the "Choose File" Window.
root.mainloop()
