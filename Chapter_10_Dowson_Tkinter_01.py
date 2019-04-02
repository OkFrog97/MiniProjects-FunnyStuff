'''
Chapter 10. GUI.
Programm 1. Easy Tkinter GUI.
'''

from tkinter import *

root = Tk () #Base window

#Window modification
root.title("Тирлим-бом-бом")
root.geometry("500x300")
app = Frame(root) # It is ramochka (frame)
app.grid()

lbl = Label(app, text ="Клянусь своим дуратским лбом!") #Creating МЕТКА inside frame
lbl.grid()

#Event-loop star
root.mainloop()