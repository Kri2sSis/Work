from random import shuffle
import test
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(test.Card(i,j))
        shuffle(self.cards)
    def rm_cards(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()