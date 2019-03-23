import BaseCardsClasses_from_Douson_book as cards 

from PlayerClass_from_Douson_book import Player as unit


class War_card (cards.Card):
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
            if v > 10:
                v = 10
        else:
            v = None
        return v
    

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
                

#----------------------MAIN----------------------
def main ():

    qwe = War_Deck ()
    qwe.populate()
    print (qwe)
    
    input()
    
if __name__ == '__main__':
    main ()