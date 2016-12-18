import random


def hit():
    import random
    numbers = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    letters = ["-of-Spades", "-of-Hearts", "-of-Clubs", "-of-Diamonds"]
    deck = []

    values = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9,
              9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    for i in numbers:
        for k in letters:
            deck.append(str(i) + k)

    # print(deck)
    deckl = zip(deck, values)
    dd = dict(deckl)
    # print(dd)



    hit = random.choice(deck)
    deck.remove(hit)
    score = dd.get(hit)

    if score == 1:
        print(hit)
        hol = input(print("play the ace high or low?"))
        if hol == "high":
            score = 11
            return hit + ' ' + "(worth " + str(score) + " points)"
        else:
            score = 1
            return hit + ' ' + "(worth " + str(score) + " points)"
    else:
        return hit + ' ' + "(worth " + str(score) + " points)"


hit()

'''
def round():
    userhand = []
    dealerhand = []
    i = 0
    while i in userhand < 21:
        userhand.append(hit())
        print("userhand")

round()
'''
'''user
.getbet()
.setbet()'''

'''
class Bet():

    def__init__(self,bet):
        self.bet = bet


    def Getbet(self):
        return self.bet

    def askbet(self)
        self.bet = int(input("place your wager")
