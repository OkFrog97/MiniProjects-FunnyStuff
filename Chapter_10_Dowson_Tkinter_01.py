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

#Button
bttn1 = Button (app, text = "Мирон - славный котомон!")
bttn1.grid()

#Second Buttom
bttn2 = Button ()
bttn2.grid()
bttn2.configure(text = "Я другая кнопка")

#Tried button
bttn3 = Button()
bttn3.grid()
bttn3["text"] = "И я, и я, и я того же мнения!"



#Event-loop star
root.mainloop()