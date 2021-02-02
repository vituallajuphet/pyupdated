from tkinter import *
from tkinter import messagebox
from data import Data


class Main:

    def __init__(self, notes):
        self.main_window = Tk(className=" Home Screen")
        self.main_window.geometry("600x300")
        self.allnotes = notes
        self.build()

    def build(self):

        this = self.main_window
        frame = Frame(this)
        btn_frame = Frame(this)
        frame.pack()
        btn_frame.pack()

        var = StringVar()
        label = Label(frame, text="Exam Note Compiler", relief=FLAT)
        label.config(font=("Courier", 20))
        label.grid(row=0, column=0, pady=(40, 60))
        # label.pack(side=LEFT)
        btn_note = Button(btn_frame, text="Notes", command=self.goto_notes, padx=20)
        btn_note.grid(row=1, column=1, padx=10)

        btn_read = Button(btn_frame, text="Read in Full", command=self.goto_read_full, padx=20)
        btn_read.grid(row=1, column=2, padx=10)

        btn_exam = Button(btn_frame, text="Exam Scramble", command=self.goto_shuffle, padx=20)
        btn_exam.grid(row=1, column=3, padx=10)
        btn_exam.config(width=13, font=17)
        
        btn_read.config(width=13, font=17)
        btn_note.config(width=13, font=17)
        self.main_window.mainloop()

    def goto_notes(self):
        from pages.notes import Notes
        self.main_window.destroy()
        note = Notes(self.allnotes)

    def goto_read_full(self):
        from pages.read_full import Readfull
        self.main_window.destroy()
        readfull = Readfull(self.allnotes)
        
    def goto_shuffle(self):
        from pages.shuffle import Shuffle
        self.main_window.destroy()
        shuffle = Shuffle(self.allnotes)

if __name__ == '__main__':
    # run main
    print("initialize data...")
    data = Data()
    main = Main(data.get_notes())


