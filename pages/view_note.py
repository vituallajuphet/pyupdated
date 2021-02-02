from tkinter import *
import tkinter as tk
from tkinter import messagebox
from time import sleep

class Viewnote:

    def __init__(self, notes, all_notes):

        self.allnotes = all_notes
        self.notes = notes

        self.main_window = Tk(className=' View Notes')
        self.main_window.geometry("600x600")
        this = self.main_window
        frame = Frame(self.main_window, width=600, height=600)
        frame.pack(fill="both", expand=True)
        self.frame_note = Frame(self.main_window, width=600, height=600)
        self.frame_note.pack()

        label = Label(frame, text="View Note Page")
        label.config(font=("Courier", 20))
        label.place(x=20, y=10)

        btnback = Button(frame, text="Back", command=self.back_page, padx=20)
        btnback.place(x=400, y=10)
        btnback.config(width=13, font=17)
       
        lbl_disc = Label(frame, text="Description:")
        lbl_disc.config(font=("Courier", 14, 'bold'))
        lbl_disc.place(x=20, y=100)

        lbl_disc_text = Message(frame, text=self.notes["description"], width=500 )
        lbl_disc_text.config(font=("Courier", 14))
        lbl_disc_text.place(x=20, y=130)    

        btnshow = Button(frame, text="Show Answer", command=self.show_answer, padx=20)
        btnshow.place(x=20, y=450)
        btnshow.config(width=13, font=17)

        self.lbl_answer = Label(frame, text="")
        self.lbl_answer.config(font=("Courier", 14, 'bold'))
        self.lbl_answer.place(x=20, y=500)

        self.main_window.mainloop()

    def back_page(self):
        from pages.notes import Notes
        self.main_window.destroy()
        note = Notes(self.allnotes)

    def show_answer(self):
        self.lbl_answer.config(text=self.notes["title"])

        return self

