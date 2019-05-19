'''
This programm imitate TV by OOP.
'''
    
#decorator ISNT WORK
def check_vol (meth):
    def wrapper (self):
        if 0 <= meth () <= 10:
            meth ()
        elif 10 < meth ():
            print ('Max volume level')
        else:
            print ('Volume off')




class TV: #TV simulator class.
    def __init__ (self, volume = 5, chanel = 1):
        self.volume = volume
        self.chanel = chanel
    
    
    @check_vol #ISNT WORK
    def volume_up (self):
        self.volume += 1
    
    
    @check_vol #ISNT WORK
    def volume_down (self):
        self.volume -= 1
    
    
    def chanel_select (self):
        user_chanel = int (input('Please choose the chenal: '))
        if 0 <= user_chanel <= 9:
            self.chanel = user_chanel
        else:
            print ('ERROR! I have not this chenal')        
    
   
    def status_report (self):
        print ('Volume level: {0}.\nCnanel: {1}.'.format(self.volume, self.chanel))
        
def main (): #main programm
    print ('''
    Welcome to TV emulator.
    Sit on the your chair and lounge.
    ''')
    
    choise = None
    
    tv = TV()

    while choise != 0:
        print ('''
        Instruction:
        0 - exit;
        1 - volume up;
        2 - volume down;
        3 - choose chenal;
        4 - check tv status;
        ''')
        
        choise = input ('Enter: ')
        
        if choise == '0':
            print ('TV off. Good night')
        elif choise == '1':
            tv.volume_up ()
        elif choise == '2':
            tv.volume_down ()
        elif choise == '3':
            tv.chanel_select ()
        elif choise == '4':
            tv.status_report ()
        else:
            print ('Wrong command. Try again.')
    del tv
        
    input ()
    
main ()
