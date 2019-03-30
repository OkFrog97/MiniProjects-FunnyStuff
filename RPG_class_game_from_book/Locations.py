class location ():
    '''
    Basic location class.
    '''
    def __init__ (self, name, discription, doors_to = None):
        self.name = name
        self.discription = discription
        self.doors_to = doors_to
    
    def __str__ (self):
        rep = '\nКомната: {0}\nОписание: {1}\nМожно пройти в: {2}\n'.format(self.name, self.discription, self.doors_to)
        return rep
    
    def connections (self, *args):
        connected_rooms = []
        for i in args:
            connected_rooms.append(i.name)
        self.doors_to = connected_rooms
  
    def is_player_here (self, player):
        if player.location == self.name:
            return True
        else:
            return False