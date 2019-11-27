import deck
import  player

class Game:
    def __init__(self):
        name1 = input("Введите имя")
        name2 = input("Введите имя")
        self.deck = deck.Deck()
        self.name1 = player.Player(name1)
        self.name2 = player.Player(name2)

    def wins(self,winner):
        print("{} забирает карты".format(winner))

    def draw(self, p1n, p1c, p2n, p2c):
        print("{} кладет {}, а {} кладет {}".format(p1n,p1c,p2n,p2c))

    def player_game(self):
        cards = self.deck.cards
        print("Поехали")
        while len(cards) >= 2:
            response = input("Нажмите Х для выхода из игра. НАжмите любую клавишу для начала игры")
            if response == "Х":
                break
            p1c = self.deck.cards()
            p2c = self.deck.cards()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        win = self.winner(self.p1, self.p2)
        print("Игра окончена выиграл {}".format(win))

    def winner(self,p1,p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Ничья!"


game = Game()
game.player_game()