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
        #Discription
        Label  (self,
                text = 'Угадай число от 1 до 100. Для ввода используй поле.'
                ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
        #Area for user input
        self.user_ent = Entry(self)
        self.user_ent.grid(row = 1, column = 0, sticky = W)
        #Starting bunnot
        Button(self,
               text = "Угадать число.",
               command = self.gess_number
               ).grid(row = 2, column = 0, sticky = W)
        #Text area.
        self.story_text = Text (self, width = 40, height = 5, wrap = WORD)
        self.story_text.grid(row = 3, column = 0, sticky = W)

    def gess_number (self):
        pass






        
def main ():
    root = Tk()
    root.title('Угадай число')
    app = Application (root)
    root.mainloop()
 
if __name__ == '__main__':
    main()
