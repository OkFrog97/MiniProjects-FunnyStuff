'''
Let's use OOP and classes for GUI.
'''

from tkinter import *

class Application (Frame):
    '''
    GUI-application with 3 buttoms.
    '''
    def _init__(self, master):
        '''Init frame
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        '''
        """ Initialize the Frame. """
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
        self.bttn3["text"] = "Один КОТ хорошо, а два - ободранные обои."
      
      
#Programm body

root = Tk()
root.title("Lazy Buttons 2")
root.geometry("200x85")
app = Application(root)
root.mainloop()