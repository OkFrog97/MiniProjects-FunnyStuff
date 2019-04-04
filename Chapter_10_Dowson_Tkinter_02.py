'''
Let's use OOP and classes for GUI.
'''

from tkinter import *

class Application (Frame):
    '''
    GUI-application with 3 buttoms.
    '''
    def _init__(self, master):
        '''Init frame'''
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        '''
        Creat 3 useless buttoms.
        '''
        #Button
        self.bttn1 = Button (self, text = "Любишь КОТаться, люби и сКОТиночку любить.")
        self.bttn1.grid()

        #Second Buttom
        self.bttn2 = Button (self)
        self.bttn2.grid()
        self.bttn2.configure(text = "Кот всему КОТова.")

        #Tried button
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "Один КОТ хорошо, а два - порванные обои."
      
      
#Programm body

def main():
    root = Tk()
    root.title('Бесполезные КОТнопки-2')
    root.geometry('400x200')
    app = Application(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()