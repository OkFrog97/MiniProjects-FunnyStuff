import BaseCardsClasses_from_Douson_book as cards 

from PlayerClass_from_Douson_book import Player as unit

class War_Account ():
    '''
    Work witj bets.
    Работа со ставками.
    '''
    def __init__ (self, money = 0):
        self.money = money
     
    def is_enough (self, sum_to_transfer): #chek money in purse.
        if self.money - sum_to_transfer >= 0:
            return True
        else:
            return False
    
    def withdraw (self, sum_to_transfer, other_account): #give money from this object and give it for other_account(object).
        if self.is_enough (sum_to_transfer):
            other_account.reciept (sum_to_transfer)
            self.money -= sum_to_transfer
        else:
            print ("Недостаточно денежных средств.")
    
    def reciept (self, sum_for_transfer): #Add money in purse.
        self.money += sum_for_transfer
     
    def how_much (self):
        return self.money


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
    
    def __init__(self, name):
        War_Hand.__init__(self, name)
        self.account = War_Account (10)
    
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
        self.bank = War_Account ()
    
    def play(self):
        #Give 1 cards for all players.
        self.deck.deal(self.players, per_hand = 1)
        for player in self.players: #Revers card. Переворачиваем карту рубашкой вверх. 
            player.flip_first_card()
            player.account.withdraw(5, self.bank)
        print ('Ставки сделаны Банк: {}'.format(self.bank.how_much()))
        print ('\nКто рискнет повысить ставку?\n')#Место для повышения ставок
        
        bets = []
        
        while let(set(bets)) != 1:
            for player in self.players:
                while True: #try-except check cycle.
                    try:
                        
                        if len(bets) == 0 or set(bets) == {0}: #if nobody did bet
                            answer = input ('Игрок {}:\nделай свою ставку?! (0/n - отказаться от повышения ставки) '.format(player))
                            if answer.lower() == '0', 'n':
                                bets.append(0)
                            else:
                                bets.append(int(answer))
                        
                        else:
                            while len(bets) < (self.players.index(player)+1):
                                bets.append (0)
                            
                            answer = input ('Игрок {0}:\n Сделана ставка {1};\nу тебя в кошельке {2};\nТвоя ставка:{3};\nПоддерживай (введи сумму ставки), повышай или пасуй (введи 0/Пас): '.format(player, max(bets), player.account.how_much(), bets[(self.players.index(player)])))
                            if int(answer) < max(bets) or player.account.is_enough(int(answer)) == False or answer == 'пас':
                                print('Сыграл и проиграл! Еще повезет!')
                                player.account.withdraw(bets[self.players.index(player)], bak) #Lose player bet go to bank
                                bets.pop(self.players.index(player)) #Lose player bet delite
                                self.players.pop(self.players.index(player)) #Lose player delite
                            else:
                                bets[self.players.index(player)] = int(answer)

                    except ValueError:
                        print ('Вы ввели не число')
                        continue
                    break    
                     
        
        
        
        
        
        '''
        #ГОВНОКОД!!!
        is_bet_made = None
        bet = None
        old_bet = 0
            
        while old_bet != bet:    
            
                for player in self.players:
                    if is_bet_made == None:
                        answer = input ('Игрок {}, повышаем ставку на? (n - отказаться от повышения ставки) '.format(player))
                        if  answer.lower() != 'n':
                            try:
                                bet = int (answer)
                                player.account.withdraw(bet, self.bank) #А если не хватает денег?
                                is_bet_made = True
                            except ValueError:
                                print ('Вы ввели не чило.')
                           
                                                        
                   
                    elif is_bet_made: 
                        answer = int(input ('Игрок {0}, предыдущим игроком сделана ставка {1}, у вас в кошельке {2}, уравнивайте (добавьте к своей ставке {3} монеты) или повышайте на: '.format(player, bet, player.account.how_much(), (bet - old_bet)))) # не меняется ставка
                        if answer < bet or player.account.is_enough(answer) == False:
                            print('Вы ввели меньшую сумму или вам не хватает средств для поддержания ставки')
                            self.players.pop(self.players.index(player))
                        elif answer >= bet:
                            player.account.withdraw(bet, self.bank)
                            old_bet = bet
                            bet = old_bet + answer
                            
       
                    
                  
            
                if is_bet_made == None: #exit while cycle.
                    old_bet = bet
        '''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        print('\n$$$БАНК$$$\n{}\n'.format(self.bank.how_much()))
        for player in self.players:
            player.flip_first_card()
            print (player)
        
        winner = [self.players[0]] #Юзаем стэк, по умолчанию вставляем первого игрока.
        for player in self.players:
            if player.total >= winner[0].total: #danger zone! Не учтена ньчия!
                winner.pop()
                winner.append (player)
        for player in self.players:
            if 1 < len(winner) and player in winner:
               player.push()
            elif player in winner:
                self.bank.withdraw(self.bank.how_much(), player.account)
                player.win()
                print ('В его кошельке {} монет!'.format (player.account.how_much()))
            else:
                player.lose()            
        
        for player in self.players:
            player.clear()


def main ():
    hello_words = """
                    ---Карточная игра---\n
                           -ВОЙНА-\n
    Играть могут от двух до шести игроков.
    Каждому игроку выдается по одной карте.
    И десять монет для того, что бы сделать ставки.
    Побеждает тот игрок, чья карта имеешь больший номинал.
    Он же забирает банк.
    Рискнешь сыграть в слепую удачу?
                  """

    print(hello_words)
    
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
