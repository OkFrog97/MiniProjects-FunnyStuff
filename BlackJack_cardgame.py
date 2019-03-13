import BaseCardsClasses_from_Douson_book, PlayerClass_from_Douson_book

class BJ_card (BaseCardsClasses_from_Douson_book.card):
    ACE_VALUE = 1
    @property
    def value (self):
        if self.is_face_up: #if True
            v = BJ_card.RANNS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None

