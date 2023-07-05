from tkinter import *
from tkinter import ttk
import random
w = Tk()
w.geometry("400x400")
w.resizable(False, False)
c = "%06x" % random.randint(0, 0xFFFFFF)
w.configure(bg=f"#{c}")
h = ttk.Label(w, text=f"HEX: #{c}")
h.pack()
g = ttk.Label(w, text=f"RGB: {tuple(int(c[i:i+2], 16) for i in (0, 2, 4))}")
g.pack()
def r():
    randCol = "%06x" % random.randint(0, 0xFFFFFF)
    w.configure(bg=f"#{randCol}")
    h.config(text=f"HEX: #{randCol}")
    g.config(text=f"RGB: {tuple(int(randCol[i:i+2], 16) for i in (0, 2, 4))}")
ttk.Button(w, text="new", command=r).pack()
w.mainloop()
