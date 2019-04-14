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
        self.likes_horrors = BoolenVar()
        Checkbutton(self, text = "Ужасы", variable=self.likes_horrors, command = self.update_text).grid(row = 3, column = 0, stick = W)
        #romatic
        self.like_romantic = BoolenVar()
        Checkbutton(self, text = "Фильмы о любви", variable=self.likes_romantic, command = self.update_text).grid(row = 4, column = 0, stick = W)
        #text area
        self.result_text = Text (self, widht = 40, height = 5, wrap = WORD)
        self.result_text.grid(row = 5, column = 0, stick = W)
    
    def update_text(self):
        likes = ""
        if self.likes_comedy.get():
            likes += "Вы смеетесь над странными шутками Эдди Мерфи.\n"
        if self.likes_horrors.get():
            likes += "Вам нравится, когда КРОВЬ КИШКИ РАСПИДОРАИСЛО!!!!\n"
        if self.likes_romantic.get():
            likes += "Где же, мистер Дарси???\n"
        self.result_text.delete(0.0, END)
        self.result_text.insert(0.0, likes)

def main ():
    root = Tk()
    root.title('QWERTY')
    app = Application (root)
    root.mainloop()
 
in __name__ == '__main__':
    main()