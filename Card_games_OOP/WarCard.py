import BaseCardsClasses_from_Douson_book as cards 

from PlayerClass_from_Douson_book import Player as unit


class War_card (cards.Card):
    RANK = ('2','3','4','5','6','7','8','9','10','J','Q','K', 'A')
    ACE_VALUE = 1
    @property
    def value (self):
        '''
        Chek catd fece and if it see return card points.
        Card points is index of card rank.
        Проверяет, перевернута ли карта рубашкой вниз, 
        и если наминал карты виден, возвращает количество очков,
        которые считаются как мндекс значения карты.
        '''
        if self.is_face_up:
            v = War_card.RANK.index(self.rank)+1
        else:
            v = None
        return v


class War_Hand (cards.Hand):
    def __init__(self, name):
        super(War_Hand, self).__init__()
        self.name = name
    
    def __str__(self):
        rep = self.name + ':\t' + super(War_Hand, self).__str__()
        if self.total:
            rep += '({})'.format(str(self.total))
        return rep
    
    @property
    def total(self):
        t = 0
        for card in self.cards:
            t += card.value
        return t


class War_Deck (cards.Deck): 
    '''
    Deck for War card geming. Import from cards.
    Колода для карточной игры Война. Импортируется из cards.
    '''
    def populate (self):
        '''
        Populate new deck by cards. (Init new cards inside deck).
        Наполняет колоду картами.
        '''
        for suit in War_card.SUITS:
            for rank in War_card.RANK:
                self.cards.append(War_card(rank, suit))

                
class War_Player (unit):
    def lose(self):
        print (self.name, ' прогирал.')
        
    def win(self):
        print (self.name, ' победил!')
        
    def push(self):
        print(self.name, ' ничья.')

        
class War_Game ():
    def __init__ (self, names):
        self.players = []
        for name in names:
            player = War_Player (name)
            self.players.append(player)
        self.deck = War_Deck()
        self.deck.populate()
        self.deck.shuffle()
    
    def play(self):
        #Give 1 cards for all players.
        self.deck.deal(self.players, per_hand = 1)
        for player in self.players: #Revers card. Переворачиваем карту рубашкой вверх. 
            self.player.flip_first_card()
        #Место для повышения ставок
        winner = [None]
        for player in self.players:
            if self.player.total >= winner[0].total:
                winner.pop()
                winner.append (self.player)
        for player in self.players:
            if 1 < len(winner) and player in winner:
               player.push()
            elif player in winner:
                player.win()
            else:
                player.lose()            
        
        
        
        
        
        
        
        '''
        self.dealer.flip_first_card()#first diller card flip
        '''
        
        
        for player in self.players:
            print (player)
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

    




















#----------------------MAIN----------------------
def main ():

    qwe = War_Deck ()
    qwe.populate()
    print (qwe)
    
    input()
    
if __name__ == '__main__':
    main ()