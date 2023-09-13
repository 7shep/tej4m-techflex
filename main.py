#Welcome to Shep's TEJ4M Tech Flex! 

import tkinter as Tk
from tkinter import Tk, PhotoImage, Label
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkVideoPlayer import TkinterVideo
import pygame as pygame
from pygame import mixer
import keyboard
import threading
import time

#Functions for the Music & Video Player 

#For pausing, using the same system as my last tech flex!
num = 0

def chooseFile():
    global chosenFile
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

def resize_image(image_path, width, height):
    img = PhotoImage(file=image_path)
    img = img.subsample(int(img.width() / width), int(img.height() / height))
    return img


def audioFile(chosenFile):
    global audio
    #print('hi') <-- Debug line.

    #Creates window for the audio file.
    audio = Tk()
    icon = PhotoImage(file='./Images/icon.png')
    audio.iconphoto(False, icon)
    audio.title("Shep's Audio Player")
    audio.geometry("1920x1080")
    audio.configure(background="#FFFFFF")
    img = resize_image("./Images/def.png", width=1920, height=750)
    label = Label(audio, image = img)
    label.pack()

    
    audioPause = Button(audio, text="Pause/Play", command=audiobutton)
    audioPause.pack()
    
    audioStop =  Button(audio, text="Stop", command=stopAudio)
    audioStop.pack()
    #print(chosenFile) <-- debug line.

    #Plays the MP3 file.
    sound = mixer.Sound(chosenFile)
    sound.play()
    
    newFile = threading.Thread(target=newAudioFile)
    newFile.daemon = True
    newFile.start()

    #Opens the GUI.
    audio.mainloop()

def audiobutton():
    global num
    if chosenFile.endswith('.wav'):
                if mixer.get_busy():
                    if (num % 2) == 0:
                        mixer.unpause()
                        print('Music Unpaused')
                        num += 1
                        
                    else:
                        mixer.pause()
                        print('Music paused')
                        num += 1

def videoFile(chosenFile):
    global videoplayer
    global video
    #print('hiii) <-- Debug line.

    #Video Gui!
    video = Tk()
    icon = PhotoImage(file='./Images/icon.png')
    video.iconphoto(False, icon)
    video.title("Shep's Video Player")
    video.geometry("1920x1080")
    video.configure(background="#FFFFFF")


    mixer.init()
    #Plays the MP4
    videoplayer = TkinterVideo(master=video, scaled=True)
    videoplayer.load(chosenFile)
    videoplayer.pack(expand=True, fill="both")
    #videoplayer.audio.set_volume(0.5)

    #videoSound = mixer.Sound(chosenFile)
    #videoSound.play()

    videoplayer.play()

    videopause = Button(video, text="Pause/Play", command = videoPause)
    videopause.pack()

    videostop = Button(video, text="Stop Video", command=stopVideo)
    videostop.pack()

    #newVideoFile = threading.Thread(target=newVideoFile(videoplayer))
    #newVideoFile.daemon = True
    #newVideoFile.start()

    #Opens the GUI.
    video.mainloop()

#Detecting Space Key

def videoPause():
    print('videopause')
    if videoplayer.is_paused():
        videoplayer.play()
    else:
        videoplayer.pause()

def stopVideo():
    print('videostop')
    videoplayer.stop()
    video.destroy()

def pauseFile():
    global num
    global chosenFile
    global videoplayer

    
    while True:
        if keyboard.is_pressed('space'):
            if chosenFile.endswith('.wav'):
                if mixer.get_busy():
                    if (num % 2) == 0:
                        mixer.unpause()
                        print('Music Unpaused')
                        num += 1
                        
                    else:
                        mixer.pause()
                        print('Music paused')
                        num += 1
                else:
                    print('Music is not playing.')
            elif chosenFile.endswith('.mp4'):
                print(videoplayer.is_paused)
        time.sleep(0.1)
        
def stopAudio():
    mixer.stop()
    audio.destroy()
    
#Changes the Audio file when R is pressed!
def newAudioFile():
    while True:
            if keyboard.is_pressed('r'):
                mixer.stop()
                newFile = askopenfilename(filetypes=[("Audio Files","*wav")])
                newSound = mixer.Sound(newFile)
                newSound.play()
            time.sleep(0.1)

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

#ALL THREADING FOR KEYBOARD FUNCTIONS!!

#Threading runs this code in the background, target is the function. It is looking for the "spaceKey" function to be called.
spacekeythread = threading.Thread(target=pauseFile)
#Setting daemon to true allows me to exit the program.
spacekeythread.daemon = True
#Starts the threading
spacekeythread.start()

#Opens the "Choose File" Window.
root.mainloop()
