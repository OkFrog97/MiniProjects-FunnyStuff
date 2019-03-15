import BaseCardsClasses_from_Douson_book as cards 

import PlayerClass_from_Douson_book as games

class BJ_Card (cards.Card):
    ACE_VALUE = 1
    @property
    def value (self):
        if self.is_face_up: #if True
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return V

class BJ_Deck (cards.Deck):
    '''BlackJack deck'''
    def populate (self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))

class BJ_Hand (cards.Hand):
    def __init__(self, name):
        cards.Hand.__init__(self) #In book: super(BJ_Hand, self).__init__()
        self.name = name
        