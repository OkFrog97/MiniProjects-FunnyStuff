class location ():
    '''
    Basic location class.
    '''
    def __init__ (self, name, discription):
        self.name = name
        self.discription = discription
    
    def __str__ (self):
        rep = 'Комната: {0}\nОписание: {1}\n'.format(self.name, self.discription)
        return rep
    
    def connections (self, *args):
        connected_rooms []
        for i in args:
            connected_rooms.append(i)
        return connected_rooms
  
    def is_player_here (self, player):
        if player.location == self.name:
            return True
        else:
            return False