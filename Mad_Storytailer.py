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
        #prilogatelnoe, ept
        Label   (self,
                text = "Выбирте прилагательное."
                ).grid(row = 4,column = 0, sticky = W)
        #Нетерпеливый
        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text = "Нетерпеливый",
                    variable = self.is_itchy
                    ).grid(row = 4, column = 1, sticky = W)
        #Радостный
        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text = "Радостный",
                    variable = self.is_joyous
                    ).grid(row = 4, column = 2, sticky = W)
        #Пронизывающий
        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text = "Пронизывающий",
                    variable = self.is_electric
                    ).grid(row = 4, column = 3, sticky = W)
        #body parts
        Label   (self,
                text = "Тела кусок выбери ты: "
                ).grid(row = 5, column = 0, sticky = W)
        self.body_parts = StringVar ()
        self.body_parts.set(None)
        #body_parts switcher
        body_parts = ["Пупок","Большой палец ноги","Продолговатый мозг"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_parts,
                        value = part
                        ).grid(row = 5, column = column, sticky = W)
            column += 1
        #Enter data and get story
        Button(self,
               text = "Получить рассказ",
               command = self.tell_story
               ).grid(row = 6, column = 0, sticky = W)
        self.story_text = Text (self, width = 75, height = 10, wrap = WORD)
        self.story_text.grid(row = 7, column = 0, columnspan = 4)
    
    def tell_story(self):
        '''write story in text area'''
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        abjectives = ''
        if self.is_itchy.get():
            abjectives += "Нетерпеливый NuRgZzliEV"
        elif is_joyous.get():
            abjectives += "Радостный"
        elif is_electric.get():
            abjectives += "Пронизывающий"
        body_part = self.body_parts.get()
        
        #Creating the story
        story = "Знаменитый путешественник {0} уже отчаялся зваершить SICHIK своей жизни - город, в котором обитали STRASHNII {1}. Однажды они столкнулись лицом к лицу и мощное {2} отразилось на лице {0}. Если задумали {3}, делайте осторожно, что бы не оторвать {4}.".format(person, noun.title(), abjectives, verb, body_part)
        
        self.story_text.delete(0.0, END)
        self.story_text.insert(0.0, story)

        
def main ():
    root = Tk()
    root.title('Безумный сказочник')
    app = Application (root)
    root.mainloop()
 
if __name__ == '__main__':
    main()
