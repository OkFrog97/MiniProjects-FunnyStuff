'''
This programm asks you gessing the number.
'''

from tkinter import *

class Application (Frame):
    '''GUI-applocation who's play in number games'''
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.creat_widgets()
    
    def creat_widgets (self):
        '''Creating widgets.'''
        Label  (self,
                text = 'Я загадал число. Попытайтесь его угадать и ввести в полне ниже.'
                ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
        