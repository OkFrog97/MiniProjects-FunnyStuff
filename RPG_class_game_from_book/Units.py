class unit ():
    '''
    Basic unit class.
    '''
    def __init__ (self, name, location = None):
        self.name = name
        self.location = location
    
    def move_to(self, location):
        self.location = location
    
    def where_am_i (self):
        return self.location