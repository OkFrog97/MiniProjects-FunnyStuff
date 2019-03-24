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

                
class War_Player (War_Hand):
    def lose(self):
        print (self.name, ' прогирал.')
        
    def win(self):
        print (self.name, ' победил!')
        
    def push(self):
        print(self.name, ' ничья.')
    
    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip() 

        
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
            player.flip_first_card()
            print (player)
        print ('Кто рискнет?')#Место для повышения ставок
        for player in self.players:
            player.flip_first_card()
            print (player)
        winner = [self.players[0]] #Юзаем стэк, по умолчанию вставляем первого игрока.
        for player in self.players:
            if player.total >= winner[0].total: #danger zone
                winner.pop()
                winner.append (player)
        for player in self.players:
            if 1 < len(winner) and player in winner:
               player.push()
            elif player in winner:
                player.win()
            else:
                player.lose()            
        
        for player in self.players:
            player.clear()


def main ():
    print('\t---Карточная игра---\n\t\t-ВОЙНА-')
    print('Играть могут от двух до шести игроков.\nКаждому игроку выдается по одной карте.\nПобеждает тот игрок, чья карта имеешь больший номинал.\n')
    names = []
    
    try:
        number = int(input('Сколько игроков играет?(2-6) '))
    except ValueError:
        print ('Вы ввели не число.')
        number = 0
    if 2 <= number <= 6: 
        for i in range(number):
            name = input('Введите имя игрока №{}: '.format(i+1))
            names.append(name)
            print()
        game = War_Game(names)
        again = None
        while again != 'n':
            game.play()
            again = input('Сыграть еще раз? (y/n) ')
    else:
        print ('Вы ввели некорретные данные. Игра будет приостановлена.')
    input('Нажмите ENTER для выхода.')

if __name__ == '__main__':
    main ()