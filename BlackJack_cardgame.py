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
    '''
    BlackJack deck.
    '''
    def populate (self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))

class BJ_Hand (cards.Hand):
    def __init__(self, name):
        cards.Hand.__init__(self) #In book: super(BJ_Hand, self).__init__()
        self.name = name
    def __str__(self):
        rep = self.name + ':\t' + super((BJ_Hand, self).__str__()
        if self.total:
            rep += '({})'.format(str(self.total))
        return rep
    @property
    def total(self):
        #if one of card value = None then all values = None; Чего, блеать?
        for card in self.cards:
            in not card.value:
                return None
        #Sum points, Ace = 1;
        t = 0
        for card in self.cards:
            t += card.value
        #Check Ace in player hand
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
        #If Player Hand have Ace and score <= 11 then Ace = 11
        if contains_ace and t <= 11:
            t+=1o
        return t
    def is_busted(self):
        return self.total > 21
    
class BJ_Player (BJ_Hand):
    '''
    Black_Jack player.
    '''
    def is_hitting(self):
        response = games.ask_yes_no('\n {}, eche cartishku? (Y/N): '.format(self.name))
        return response == 'y'
    def bust(self):
        print (self.name, 'ups...perebral.')
        self.lose()
    def lose(self):
        print (self.name, 'proigral. Nichego, bratok, esche povezet.')
    def win(self):
        print (self.name, 'wiigral, zoebis, krasava')
    def push(self):
        print(self.name, 'op, nihuia, nichia, vnature! Nado povtorit!')
        