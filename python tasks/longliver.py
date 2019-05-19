from tkinter import *

class Application(Frame):
    def __init__ (self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.creat_widgets()
      
    def creat_widgets(self):
        self.inst_lbl = Label(self, text = "Чтобы узнать секрет долголетия, введите пароль.")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        self.pw_lbl = Label(self, text = "Пароль: ")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)
        
        
        
        
        
root = Tk()
root.title("Счетчник щелчков")
root.geometry("400x50")
app = Application(root)
root.mainloop()