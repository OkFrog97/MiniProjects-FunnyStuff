import BaseCardsClasses_from_Douson_book as cards 

from PlayerClass_from_Douson_book import Player as games

class BJ_Card (cards.Card):
    ACE_VALUE = 1
    @property
    def value (self):
        if self.is_face_up: #if True
            v = BJ_Card.RANK.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck (cards.Deck):
    '''
    BlackJack deck.
    '''
    def populate (self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANK:
                self.cards.append(BJ_Card(rank, suit))

class BJ_Hand (cards.Hand):
    def __init__(self, name):
        cards.Hand.__init__(self) #In book: super(BJ_Hand, self).__init__()
        self.name = name
    def __str__(self):
        rep = self.name + ':\t' + super(BJ_Hand, self).__str__()
        if self.total:
            rep += '({})'.format(str(self.total))
        return rep
    @property
    def total(self):
        #if one of card value = None then all values = None; Чего, блеать?
        for card in self.cards:
            if not card.value:
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
            t += 10
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
        print (self.name, 'wiigral, zoebis, krasava.')
    def push(self):
        print(self.name, 'op, nihuia, nichia, vnature! Nado povtorit!')

class BJ_Dealer (BJ_Hand):
    def is_hitting(self):
        return self.total < 17
    def bust(self):
        print (self.name, 'Zdaiushii malen\'ko perebral. A vam fartit!')
    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()
'''
class BJ_Game(object):
    """ A Blackjack Game. """
    def __init__(self, names):      
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Dealer")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
           
    def play(self):
        # deal initial 2 cards to everyone
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()    # hide dealer's first card
        for player in self.players:
            print(player)
        print(self.dealer)

        # deal additional cards to players
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()    # reveal dealer's first 

        if not self.still_playing:
            # since all players have busted, just show the dealer's hand
            print(self.dealer)
        else:
            # deal additional cards to dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                # everyone still playing wins
                for player in self.still_playing:
                    player.win()                    
            else:
                # compare each player still playing to dealer
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        # remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()
'''      

class BJ_Game ():
    def __init__ (self, names):
        self.players = []
        for name in names:
            player = BJ_Player (name)
            self.players.append(player)
        self.dealer = BJ_Dealer('Dealer')
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
    
    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp
   
    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print (player)
            if player.is_busted():
                player.bust()

    def play(self):
        #Give 2 cards for all players.
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()#first diller card flip
        for player in self.players:
            print (player)
        print(self.dealer)
        #Сдача дополнительных карт
        for player in self.players:
            self.__additional_cards(player)
        self.dealer.flip_first_card() #Раскрывается первая карта дилера
        if not self.still_playing:
            print (self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)
            if self.dealer.is_busted():
                for player in self.still_playing:
                    player.win()
                else:
                    for player in self.still_playing:
                        if player.total > self.dealer.total:
                            player.win()
                        elif player.total < self.dealer.total:
                            player.lose()
                        else:
                            player.push()
        for player in self.players:
            player.clear()
        self.dealer.clear()



def main():
    print ('\t\tVelkom to rashen Chernii Vanek, epta (Russian Black Jack without Bender Rodriges).')
    names = []
    number = games.ask_number("Skolko pacanov igraet? (1-7) ", low = 1, high = 8)
    for i in range(number):
        name = input('Kak zvat bratan?: ')
        names.append(name)
        print()
    game = BJ_Game(names)
    again = None
    while again != 'n':
        game.play()
        again = games.ask_yes_no('Esche razok?')
        main()
    input('Jmi Entet chtobi exit.')

if __name__ == '__main__':
    main()    
