'''
This programm say how you can living a long time.
'''

from tkinter import *

class Application (Frame):
    '''
    GUI-application.
    '''
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()
    
    def create_widget(self):
        #text instruction
        self.inst_lbl = Lable (self, text = "Введите пароль \"secret\" что-бы узнать секрет долголетия: ")
        self.init_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        self.pw_lbl = Lable(self, text = "Пароль")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)