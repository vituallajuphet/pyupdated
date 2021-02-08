from tkinter import *
import tkinter as tk
from tkinter import messagebox
from time import sleep
from tkinter import ttk


class Notes:

    def __init__(self, notes):

        self.all_notes = notes

        self.main_window = Tk(className=' Notes')
        self.main_window.geometry("600x800")
        this = self.main_window
        frame = Frame(self.main_window, height=200)
        frame.pack(side=TOP, fill=BOTH, expand=0)

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
       
        label3 = Label(frame, text="Your Notes:")
        label3.place(x=20, y=160)
        label3.config(font=("Courier", 18, 'bold'))


        canFrame = Frame(self.main_window)
        canFrame.pack(fill=BOTH, expand=1)
        # canFrame.place(x=0, y=200)

        my_canvas = Canvas(canFrame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scrollbar = ttk.Scrollbar(canFrame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        self.lastframe = Frame(my_canvas)
        my_canvas.create_window((0,0), window=self.lastframe, anchor="nw")

         

        self.generate_notes()
        self.main_window.mainloop()

    def generate_notes(self):
        print("generating notes...")
        base_y = 70
        i = 0
        btn=[]

       

        for note in self.all_notes:
            btn.append(Button(self.lastframe, text="View Note", width=13, font=17, padx=20))
            # btn[i].place(x=20, y=base_y)
            btn[i].grid(row=i, column=0, pady=10, padx=10)
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




