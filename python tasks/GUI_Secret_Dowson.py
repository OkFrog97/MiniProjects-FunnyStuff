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
        self.inst_lbl = Label (self, text = "Введите пароль \"secret\" что-бы узнать секрет долголетия: ")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        #password
        self.pw_lbl = Label(self, text = "Пароль")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)
        #entry widget to accept password
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)
        #enter button
        self.subbmit_bttn= Button(self, text = "Узнать секрет.", command = self.reveal)
        self.subbmit_bttn.grid(row = 2, column = 0, sticky = W)
        #text massage to display answer
        self.secret_txt = Text (self, width = 30, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 3, column = 0, sticky = W)
     
    def reveal(self):
        '''
        Data cut and insert.
        '''
        contents = self.pw_ent.get()
        if contents == "secret":
            message = "Что-бы дожить до ста лет, нужно дожить до 99 лет...\n...а потом вести себя ооооочень осторожно."
        else:
            message = "Не тот пароль. Как же дожить до ста лет, если строчку сверху прочитать не получилось?"
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)

def main():
    root = Tk()
    root.title("Долгожитель")
    root.geometry("450x200")
    app = Application(root)
    root.mainloop()

if __name__ == "__main__":
    main()

    
    
    
    
