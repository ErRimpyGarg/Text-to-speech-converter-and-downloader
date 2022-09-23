#STEP:1 Importing required modules and setting window screen.

from tkinter import *
from tkinter import messagebox

import pyttsx3

window = Tk()
window.title("Text to speech downloader")
window.config(bg="steel blue", border="10", relief="groove")
window.geometry("650x680")

#STEP:2 Creating heading text label
heading = Label(window, text="Add Text Below", font=("Roman", 17, "bold"), bg="#92b09a",
                 fg="Blue", width="80", border="5", height="1")
heading.pack(pady="10")

#STEP:3 Creating Text_Area for the user to add text

text_area=Text(window, height="17", bg="#92b09a", fg="blue", font=("roman", 15))
text_area.pack(pady="10")

#STEP:4 Creating dropdown list for the selection of male and female voice

options = ["Male", "Female"]
clicked = StringVar()
clicked.set("Select Gender")

drop_down = OptionMenu(window, clicked, *options)
drop_down.pack(pady="7")

#STEP:7 Defining function for playing sound based on gender selection.

def play_sound():
    speaker = pyttsx3.init()
    list_of_voices = speaker.getProperty('voices')
    text_to_convert = text_area.get(1.0, END)
    gender_option = clicked.get()

    if gender_option == "Male":
        speaker.setProperty('voice', list_of_voices[0].id)
        speaker.say(text_to_convert)

    elif gender_option == "Female":
        speaker.setProperty('voice', list_of_voices[1].id)
        speaker.say(text_to_convert)
    speaker.runAndWait()

#STEP:5 Creating button for playing sound

play_sound_btn = Button(window, text="Play Sound", font=("Roman", 13, "bold"), border="5", fg="blue", bg="#92b09a", command=play_sound)
play_sound_btn.pack(pady="10")

#STEP:8 Defining function for downloading played sound as mp3 file in the given path.

def download_sound():
    speaker = pyttsx3.init()
    list_of_voices = speaker.getProperty('voices')
    text_to_convert = text_area.get(1.0, END)
    gender_option = clicked.get()
    speaker.save_to_file(text_to_convert, f"voice-{gender_option}.mp3")
    speaker.runAndWait()
    messagebox.showinfo("Success", "Your file has been successfully saved.")

#STEP:6 Creating button for downloading audio

download_btn = Button(window, text="Download Audio", font=("Roman", 13, "bold"), fg="blue", bg="#92b09a", border="5", command=download_sound)
download_btn.pack(pady=10)

window.mainloop()

