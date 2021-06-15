from tkinter import *
from pytube import YouTube

window = Tk()

window.title("Download Manager")

window.geometry('250x150')

lbl = Label(window, text="Link do Vídeo", pady=10)

lbl.grid(column=0, row=0)

txt = Entry(window,width=35)

txt.grid(column=0, row=1)

def clicked():
    inputValue = txt.get()
    video = YouTube(inputValue)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path="./")
    print(inputValue)

btn = Button(window, text="Download", command=clicked)

btn.grid(column=0, row=2, padx=95)

window.mainloop()