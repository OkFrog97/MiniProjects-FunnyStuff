import Locations, Units

class Game ():
    def __init__ (self, player, A, B, C):
        
        self.player = Units.unit(Fred)
        self.A = Locations.location('A', 'Empty room')
        self.B = Locations.location('B', 'Empty room')
        self.C = Locations.location('C', 'Empty room')
    
    def constructor (self):
        
        self.A.connections(self.B)
        self.B.connections(self.A, self.B)
        self.C.connections(self.B)
        
        self.player.move_to(self.B)
        
    def play (self):
        pass