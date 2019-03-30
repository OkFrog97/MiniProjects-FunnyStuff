import Locations, Units

class Game ():

    def __init__ (self):
        self.player = Units.unit('Fred')
        self.A = Locations.location('A', 'Just empty room')
        self.B = Locations.location('B', 'Room with two door')
        self.C = Locations.location('C', 'Another empty room')
    
        self.rooms_map = {'A' : self.A,
                          'B' : self.B,
                          'C' : self.C}
            
    
    def constructor (self):
        
        self.A.connections(self.B)
        self.B.connections(self.A, self.C)
        self.C.connections(self.B)
        
        self.player.move_to(self.B)
        
    def play (self):
        command = None
        while command != 'exit':
            print ('Your name is {0}. You in: {1}\nEnter name of room or "exit" to exit'.format(self.player.name, self.player.where_am_i()))
            command = input ('Your command: ')
            if command != 'exit':
                self.player.move_to(self.rooms_map[command])

def main ():
    
    hello_words = 'Welcom in SIMPL_OOP_RPG'
    game = Game ()
    game.constructor ()
    
    print (hello_words)
    game.play()
    
    input ()
    
if __name__ == '__main__':
    main()