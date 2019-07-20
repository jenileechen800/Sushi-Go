from Cards.Card import Card
from random import shuffle

class CardDeck:

    def __init__(self):
        self.cardDeck = []
        self.add_cards()
        self.awkward_shuffle()

    def add_cards(self):
        self.add_maki()
        self.add_tempura()
        self.add_sashimi()
        self.add_dumplings()
        self.add_pudding()
        self.add_chopsticks()
        self.add_wasabi()
        self.add_nigiri()

    def add_tempura(self):
        for i in range(14):
            self.cardDeck.append(Card("Tempura"))

    def add_sashimi(self):
        for i in range(14):
            self.cardDeck.append(Card("Sashimi"))

    def add_dumplings(self):
        for i in range(14):
            self.cardDeck.append(Card("Dumpling"))

    def add_nigiri(self):
        for i in range(10):
            self.cardDeck.append(Card("Salmon Nigiri"))

        for i in range(5):
            self.cardDeck.append(Card("Squid Nigiri"))

        for i in range(5):
            self.cardDeck.append(Card("Egg Nigiri"))

    def add_pudding(self):
        for i in range(10):
            self.cardDeck.append(Card("Pudding"))

    def add_chopsticks(self):
        for i in range(4):
            self.cardDeck.append(Card("Chopsticks"))

    def add_wasabi(self):
        for i in range(4):
            self.cardDeck.append(Card("Wasabi"))

    def add_maki(self):
        for i in range(12):
            self.cardDeck.append(Card("Maki(2)"))
        for i in range(8):
            self.cardDeck.append(Card("Maki(3)"))
        for i in range(6):
            self.cardDeck.append(Card("Maki(1)"))

    def awkward_shuffle(self):
        list_card_deck = [[card] for card in self.cardDeck]
        temporary_list = []
        shuffle(list_card_deck)

        for sublist in list_card_deck:
            for item in sublist:
                temporary_list.append(item)

        self.cardDeck = temporary_list












