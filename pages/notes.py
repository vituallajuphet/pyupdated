from tkinter import *
import tkinter as tk
from tkinter import messagebox
from time import sleep

class Notes:

    def __init__(self, notes):

        self.all_notes = notes

        self.main_window = Tk(className=' Notes')
        self.main_window.geometry("600x600")
        this = self.main_window
        frame = Frame(self.main_window, width=600, height=130)
        frame.pack(fill="both", expand=True)
        self.frame_note = Frame(self.main_window, width=600, height=600)
        self.frame_note.pack()

        label = Label(frame, text="Notes Page")
        label.config(font=("Courier", 20))
        label.place(x=20, y=10)
        btn_note = Button(frame, text="+ Add Note", command=self.add_note, padx=20)
        btn_note.place(x=20, y=70)
        btn_note.config(width=13, font=17)

        btnback = Button(frame, text="Back", command=self.back, padx=20)
        btnback.place(x=400, y=10)
        btnback.config(width=13, font=17)

        # frame notes
        label2 = Label(self.frame_note, text="Your Notes:")
        label2.config(font=("Courier", 18, 'bold'))
        label2.place(x=20, y=10)

        self.generate_notes()
        self.main_window.mainloop()

    def generate_notes(self):
        print("generating notes...")
        base_y = 70
        i = 0
        btn=[]
        for note in self.all_notes:
            btn.append(Button(self.frame_note, text="View Note", width=13, font=17, padx=20))
            btn[i].place(x=20, y=base_y)
            btn[i]["command"] = lambda i=note: self.view_note(i)
            base_y += 40
            i += 1
        return self

    def add_note(self):
        from pages.add_note import Addnote
        self.main_window.destroy()
        addnote = Addnote(self.all_notes)
        
        return self

    def view_note(self, notes):
        from pages.view_note import Viewnote
        self.main_window.destroy()
        viewnote = Viewnote(notes, self.all_notes)
        return self

    def back(self):
        from main import Main
        self.main_window.destroy()
        main = Main(self.all_notes)

        return self




