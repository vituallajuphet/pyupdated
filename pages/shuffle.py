from tkinter import *
import tkinter as tk
from tkinter import messagebox
from time import sleep
import random

class Shuffle:

    def __init__(self, all_notes):
        
        self.ans=[]
        self.allnotes = all_notes
        self.dummy_notes = all_notes

        self.main_window = Tk(className='Exam Scrumble')
        self.main_window.geometry("600x1000")
        this = self.main_window
        frame = Frame(self.main_window, width=600, height=140)
        frame.pack()
        self.frame_note = Frame(self.main_window, width=600, height=1000)
        self.frame_note.pack()

        label = Label(frame, text="Exam Scrumble")
        label.config(font=("Courier", 20))
        label.place(x=20, y=10)

        btnback = Button(frame, text="Back", command=self.back_page, padx=20)
        btnback.place(x=400, y=10)
        btnback.config(width=13, font=17)

        label = Label(frame, text="Enter Number of Entries: ")
        label.config(font=("Courier", 13))
        label.place(x=20, y=68)

        self.text_total = Text(frame, width=5, height=1)
        self.text_total.config(font=("Courier", 17))
        self.text_total.place(x=270, y=68)

        label = Label(frame, text=("Limit: {}".format(len(self.allnotes))))
        label.config(font=("Courier", 13))
        label.place(x=370, y=68)

        btn_generate = Button(frame, text="Generate Shuffle Notes", command=self.generate_notes, padx=20)
        btn_generate.place(x=20, y=106)
        btn_generate.config(width=20, font=17)

        # self.generate_notes()

        self.main_window.mainloop()

    def back_page(self):
        from main import Main
        self.main_window.destroy()
        main = Main(self.allnotes)

    def generate_notes(self):
        tot = 0
        txt = self.text_total.get("1.0","end-1c")
        try:
            if txt == "":
                messagebox.showerror("Error", "Please add a number of entries")
                return
            
            tot = int(txt)

            if tot > len(self.allnotes):
                messagebox.showerror("Error", "There are only {} notes!".format(len(self.allnotes)))
                return
        except:
            messagebox.showerror("Error", "Please input a number only!")
            return

        print("generating notes...")
        self.remove_child_frame_elem()
        base_y = 50
        i = 0
        btn=[]
        lbl=[]
        self.ans = []

        self.dummy_notes = self.allnotes

        shuffle_notes = random.sample(self.dummy_notes, tot)

        for note in shuffle_notes:

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

    def remove_child_frame_elem(self):
        for child in self.frame_note.winfo_children():
            child.destroy()

        return self

    def show_ans(self, answer):
        idx = answer["index"]
        self.ans[idx].config(text=answer["title"])
        return self

