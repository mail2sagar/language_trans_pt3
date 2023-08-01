from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.title("LANGUAGE TRANSLATOR")
root.geometry("600x600")
root.config(background="lavender")

title = Label(root,text="🌷⭐ Language Translator ⭐🌷",bg="misty rose",font=("Great Vibes",20,"bold"))
title.place(relx=0.5,rely=0.1,anchor=CENTER)

enter_text_label = Label(root,text="👇 ENTER TEXT HERE 👇",bg="lavender blush",font=("Times",10))
enter_text_label.place(relx=0.15,rely=0.3,anchor=CENTER)

sentence = Text(root,height=11,width=30)
sentence.place(relx=0.22,rely=0.5,anchor=CENTER)

get_text_label = Label(root,text="👇 OUTPUT 👇",bg="lavender blush",font=("Times",10))
get_text_label.place(relx=0.7,rely=0.3,anchor=CENTER)

sentence2 = Text(root,height=11,width=30)
sentence2.place(relx=0.78,rely=0.5,anchor=CENTER)


btn1 = Button(root,text="Translate",bg="lavender blush",font=("Times",18))
btn1.place(relx=0.5,rely=0.78,anchor=CENTER)

root.mainloop()