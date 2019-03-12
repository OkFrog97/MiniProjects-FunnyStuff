class Card:
    '''
    Base class for card game. Classic cards.
    '''
    RANK = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
    SUITS = ('c','d','h','s')
    def __init__ (self, rank, suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up #card face up = True; card face down = False;
    def __str__ (self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = 'XX'
        return rep
    def flip (self): #card flip
        self.is_face_up = not self.is_face_up

class Hand:
    '''
    List of cards in player hands.
    '''
    def __init__ (self):
        self.cards = []
    def __str__ (self):
        if self.cards: #Not empty = True or just nothing
            rep = ''.join(i+'\t' if self.card.index(i) != len(self.cards) - 1 else i for i in self.cards)
        else:
            rep = '<empty>'
        return rep
    def clear (self):
        self.cards = []
    def add (self, card):
        self.cards.append(card)
    def give (self, card, other_hand):
        self.cardds.remove(card)
        other_hand.add(card)
    
class Deck (Hand):
    '''
    Deck of game cards.
    '''
    def populate (self):
        for suit in Card.SUITS:
            for rank in card.RANKS:
                self.add(Card(rank, suit))
    def shuffle (self):
        import random
        random.shuffle(self.cards)
    def deal (self, hands, per_hand = 1):
        for rounds in range (per_hand):
            for hand in hands:
                if self.card:
                    top_card = self.cards [0]
                    self.give (top_card, hand)
                else:
                    print ('Cards is over')
    