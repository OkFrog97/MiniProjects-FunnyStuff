#Flags programm

from tkinter import *

class Application (Frame):
    def __init__ (self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        Label(self, text = "Укажите ваши любимые жанры кино").grid(row = 0, column = 0, sticky = W)
        Label (self, text = "Выберите один").grid(row = 1, column = 0, sticky = W)
        self.favorite = StringVar ()
        self.favorite.set(None)
        Radiobutton(self,
                    text = "Comedy",
                    variable = self.favorite,
                    value = "Comedy",
                    command = self.update_text
                    ).grid(row=2, column=0, sticky = W)
        Radiobutton(self,
                    text = "Horror",
                    variable = self.favorite,
                    value = "Horror",
                    command = self.update_text
                    ).grid(row=3, column=0, sticky = W)
        Radiobutton(self,
                    text = "Romantic",
                    variable = self.favorite,
                    value = "Romantic",
                    command = self.update_text
                    ).grid(row=4, column=0, sticky = W)
        self.result_text = Text(self, width = 40, height = 5, wrap = WORD)
        self.result_text.grid(row=5, column=0, columnspan = 3)
        
    def update_text(self):
        message = "Your favorite films is {}.".format(self.favorite.get())
        self.result_text.delete(0.0, END)
        self.result_text.insert(0.0, message)


        
def main ():
    root = Tk()
    root.title('QWERTY')
    app = Application (root)
    root.mainloop()
 
if __name__ == '__main__':
    main()
