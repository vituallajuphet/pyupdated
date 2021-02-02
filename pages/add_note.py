from tkinter import *
import tkinter as tk
from tkinter import messagebox
from time import sleep

class Addnote:

    def __init__(self, all_notes):

        self.allnotes = all_notes

        self.main_window = Tk(className=' Add Note')
        self.main_window.geometry("600x600")
        this = self.main_window
        frame = Frame(self.main_window, width=600, height=130)
        frame.pack(fill="both", expand=True)

        label = Label(frame, text="Add Note")
        label.config(font=("Courier", 20))
        label.place(x=20, y=10)

        btnback = Button(frame, text="Back", command=self.back_page, padx=20)
        btnback.place(x=400, y=10)
        btnback.config(width=13, font=17)

        label = Label(frame, text="Answer/ Title")
        label.config(font=("Courier", 16))
        label.place(x=20, y=60)

        self.text_title = Text(frame, width=20, height=1)
        self.text_title.config(font=("Courier", 16))
        self.text_title.place(x=20, y=100)

        label2 = Label(frame, text="Description / Content:")
        label2.config(font=("Courier", 16))
        label2.place(x=20, y=160)

        self.text_desc = Text(frame, width=40, height=10)
        self.text_desc.config(font=("Courier", 16))
        self.text_desc.place(x=20, y=200)

        btnsave = Button(frame, text="Save", command=self.save_data, padx=20)
        btnsave.place(x=20, y=450)
        btnsave.config(width=13, font=17)
       
        self.main_window.mainloop()

    def back_page(self):
        from pages.notes import Notes
        self.main_window.destroy()
        note = Notes(self.allnotes)
    
    def save_data(self):
        title = self.text_title.get("1.0","end-1c")
        desc = self.text_desc.get("1.0","end-1c")
        
        if title =="" or desc == "":
            messagebox.showerror("Error", "Fields must not be empty!")
            return
        
        data = {
            "title": title,
            "description": desc
        }
        self.allnotes.append(data)
        messagebox.showinfo("Success", "Saved Successfully!")
        self.text_title.delete(1.0,"end")
        self.text_desc.delete(1.0,"end")
        





