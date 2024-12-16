from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gtts import gTTS
import os

def text_to_speech():
    text=myinput.get().strip()
    if text:
        speech=gTTS(text=text,lang="en")
        filename="converted_text.mp3"
        speech.save(filename)
        os.system(f"start {filename}")
        messagebox.showinfo(title="Success",message="convert complete")
    else:
        messagebox.showwarning(title="failed",message="Error,enter some text")    

def exit_app():
    root.quit()

def clear_text(): 
    myinput.delete("0",END) 
    messagebox.showinfo("Info", "Text cleared")

root = Tk()
root.title("My frame ")
root.geometry("600x400")


mylabel = Label(root, text="Text to Speech",fg="black", font=("Arial", 30, "bold"))
mylabel.pack(pady=10)

my_sec_label = Label(root, text="Enter your text",fg="black", font=("Arial", 20))
my_sec_label.pack(pady=10)

myinput = Entry(root, width=45,font=("Arial", 15))
myinput.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=10)


btn_play =Button(button_frame, text="Play",bg="grey" ,command=text_to_speech)
btn_play.pack(side=LEFT, padx=10)

btn_exit = Button(button_frame, text="Set", bg="blue",padx=25, command=exit_app)
btn_exit.pack(side=LEFT, padx=10)

btn_set = Button(button_frame, text="Exit", bg="red",command=clear_text)
btn_set.pack(side=LEFT, padx=10)
root.mainloop()