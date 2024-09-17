from tkinter import *
from tkinter import ttk

root = Tk()

class AutoClickerView():
    def main_screen(self):
        root.title("AutoClicker")
        main_frame = ttk.Frame(root, padding="3 3 20 20")
        main_frame.grid(column=1, row=1, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        ttk.Label(main_frame, text="a").grid(column=3, row=2, sticky=W)
        root.mainloop()

a = AutoClickerView()
a.main_screen()
