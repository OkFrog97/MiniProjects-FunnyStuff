#Flags programm

from tkinter import *

class Application (Frame):
    def __init__ (self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        Label(self, text = "Укажите ваши любимые жанры кино").grid(row = 0, column = 0, sticky = W)
        Lable (Self, text = "Выберите все, что вам по вкусу").grid(row = 1, column = 0, sticky = W)
        #comedy
        self.likes_comedy = BoolenVar()
        Checkbutton(self, text = "Комедия", variable=self.likes_comedy, command = self.update_text).grid(row = 2, column = 0, stick = W)
        #horrors
        Checkbutton(self, text = "Ужасы", variable=self.likes_comedy, command = self.update_text).grid(row = 3, column = 0, stick = W)
        #romatic
        Checkbutton(self, text = "Фильмы о любви", variable=self.likes_comedy, command = self.update_text).grid(row = 4, column = 0, stick = W)
        

