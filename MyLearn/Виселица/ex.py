


def word(words):
    life = 6
    loop = True
    lens = len(words)
    enemyWords = []
    for i in range(lens):
        enemyWords.append("_")
    print(*enemyWords)
    while loop:
        letter =input("Введите букву: ")
        try:
            enemyWords[words.index(letter)] = letter
            print(*enemyWords)
            words[words.index(letter)] = "$"
        except:
            life -= 1
            print("Вы не угадали букву , попробуйте еще!! У вас осталось {}".format(life))
            print(*enemyWords)
            if life == 0:
                print("Вы проиграли!!")
                loop = False
        if "_" not in enemyWords:
            print("Вы выиграли!!!")
            loop = False




word("space")