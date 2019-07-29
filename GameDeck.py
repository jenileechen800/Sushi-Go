from Cards.CardDeck import CardDeck


class GameDeck:
    def __init__(self, num_players):
        self.card_deck = CardDeck().cardDeck
        self.game_deck = []
        self.split_list(num_players)

    def split_list(self, num_players):
        if num_players == 2:
            self.split(2, 10)
        elif num_players == 3:
            self.split(3, 9)
        elif num_players == 4:
            self.split(4, 8)
        elif num_players == 5:
            self.split(5, 7)
        else:
            print("That is not an acceptable number of players for SushiGo:(")

    # splits randomized list
    # by removing first 'n' items and adding them to 'game_deck' in form of 'mini_deck'
    def split(self, num_players, split_size):
        counter = 0
        for player in range(num_players):
            mini_deck = MiniDeck(self.card_deck[0:split_size], str(counter))
            del self.card_deck[:split_size]
            self.game_deck.append(mini_deck)
            counter += 1

    def card_in_deck(self, selected_card, deck):
        for card in deck:
            if card.name == getattr(selected_card, "name"):
                return True
        return False

class MiniDeck:
    def __init__(self, deck, name):
        self.deck = deck
        self.name = name
        self.size = len(deck)


"""
Do we want to show each mini deck one at a time(?)
Yes --> That way players can pick a card out

for mini_deck in deck:
    for player in players:
        gamedeck.pick_card(player, mini_deck)
"""
