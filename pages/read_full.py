from tkinter import *
import tkinter as tk
from tkinter import messagebox
from time import sleep

class Readfull:

    def __init__(self, all_notes):
        
        self.ans=[]
        self.allnotes = all_notes

        self.main_window = Tk(className=' Read in full')
        self.main_window.geometry("600x1000")
        this = self.main_window
        frame = Frame(self.main_window, width=600, height=50)
        frame.pack()
        self.frame_note = Frame(self.main_window, width=600, height=600)
        self.frame_note.pack()

        label = Label(frame, text="Read in full")
        label.config(font=("Courier", 20))
        label.place(x=20, y=10)

        btnback = Button(frame, text="Back", command=self.back_page, padx=20)
        btnback.place(x=400, y=10)
        btnback.config(width=13, font=17)
       
        # lbl_disc = Label(frame, text="Description:")
        # lbl_disc.config(font=("Courier", 14, 'bold'))
        # lbl_disc.place(x=20, y=100)
        self.generate_notes()

        self.main_window.mainloop()

    def back_page(self):
        from main import Main
        self.main_window.destroy()
        main = Main(self.allnotes)

    def generate_notes(self):
        print("generating notes...")
        base_y = 50
        i = 0
        btn=[]
        lbl=[]
        
        for note in self.allnotes:

            lbl.append(Message(self.frame_note, text=("{}. {}".format(i+1, note["description"])), width=560))
            lbl[i].config(font=("Courier", 12))
            lbl[i].place(x=20, y=base_y)

            btn.append(Button(self.frame_note, text="View Answer", width=13, font=13, padx=10))
            btn[i].place(x=20, y=(base_y + 40))
            note["index"] = i
            btn[i]["command"] = lambda i=note: self.show_ans(i)

            self.ans.append(Label(self.frame_note, text=""))
            self.ans[i].config(font=("Courier", 13, "bold"))
            self.ans[i].place(x=180, y=base_y + 43)

            base_y += 100
            i += 1
        return self


    def show_ans(self, answer):
        idx = answer["index"]
        self.ans[idx].config(text=answer["title"])
        return self

