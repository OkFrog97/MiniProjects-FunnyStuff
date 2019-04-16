'''
This programm tell the story. The scary random story.
'''

from tkinter import *

class Application (Frame):
    '''GUI-applocation who's creating story basic on user input.'''
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.creat_widgets()
    
    def creat_widgets (self):
        '''Creating widgets.'''
        Label  (self,
                text = 'Давай напишем историю, которой позавидуют боги.'
                ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
        #Name of charater
        Label  (self,
                text = "Имя героя: "
                ).grid(row = 1, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 0, sticky = W)
        #Noun
        Label   (self,
                text = "Введите существительное во множественном числе: "
                ).grid(row = 2, column = 0, sticky = W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row = 2, column = 1, sticky = W)        
        #Verb
        Label   (self,
                text = "Введите глагол в инфинитиве: "
                ).grid(row = 3, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 3,column = 1, sticky = W)


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
def main ():
    root = Tk()
    root.title('Безумный сказочник')
    app = Application (root)
    root.mainloop()
 
if __name__ == '__main__':
    main()
