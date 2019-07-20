from src.Player import Player
from Cards.GameDeck import GameDeck


class PlayGame:
    def __init__(self):
        self.players = []
        self.text_introduction()
        self.game_deck = GameDeck(len(self.players))

        self.play_game()

    def play_game(self):
        for i in range(3):
            self.line_break()
            print("Round " + str(i))

            self.play_round()
        self.total_points()
        self.print_winners()

    def play_round(self):
        for mini_deck in self.game_deck.game_deck:
            for player in self.players:
                self.pick_card(player, mini_deck)

    def pick_card(self, player, mini_deck):
        self.line_break()
        print(self.show_deck(mini_deck))

        selected_card = input("\n\n<<<" + player.name + ">>> please type selected card: \n").lower()

        while not self.card_in_deck(player, selected_card, mini_deck):
            self.line_break()
            print(self.show_deck(mini_deck))
            print("This card was not found in the card deck, please try again\n")
            selected_card = input("Please type selected card: \n").lower()


    def card_in_deck(self, player, selected_card, mini_deck):
        for card in mini_deck:
            if selected_card.lower() == card.name.lower():
                player.add_card(card)
                mini_deck.remove(card)

                print("<<<" + selected_card + ">>> has been added to " + player.name + "\'s deck")

                if selected_card.lower() == "chopsticks":
                    self.pick_card(player, mini_deck)
                    self.pick_card(player, mini_deck)
                return True

        return False

    def show_deck(self, mini_deck):
        card_names = []
        for card in mini_deck:
            card_names.append(card.name)

        return card_names

    def text_introduction(self):
        self.line_break()
        print("\n\nWelcome to SushiGo:).")
        self.instructions()

        self.line_break()
        num_players = input("Please enter the # of players (2-5 players)\n")

        # while num_players.__class__ != int or 2 <= num_players <= 5:
        #     print("\n\nSorry, the number of players must be a number between 2 and 5")
        #     num_players = input("Please enter the # of players (2-5 players)\n")

        self.line_break()
        for player in range(int(num_players)):
            player = Player(input("Please enter player" + str(player) + " name\n"))
            self.players.append(player)

    def instructions(self):
        read_instructions = input("Would you like to read the instructions? (y/n)\n")

        if (read_instructions == "y"):
            print("Instructions:)")

    def total_points(self):
        self.maki_points()
        self.pudding_points()

        for player in self.players:
            player.total_points()

        # sort 'players' list from largest to smallest

    def print_winners(self):
        self.line_break()
        print("And the winners are...by max number of points: ")
        for i in range(len(self.players)):
            print(str(i) + ". " + self.players[i])

    def maki_points(self):
        max_maki_count = 0
        max_maki_player = Player("player")

        second_maki_count = 0
        second_maki_player = Player("player")

        for player in self.players:
            if player.get_maki() > max_maki_count:
                max_maki_count = player.get_maki()
                max_maki_player = player

            elif player.get_maki() > second_maki_count:
                second_maki_count = player.get_maki()
                second_maki_player = player

        max_maki_player.add_points(6)
        second_maki_player.add_points(3)

    def pudding_points(self):
        max_pudding_count = 0
        max_pudding_player = Player("player")
        for player in self.players:
            if player.get_pudding() > max_pudding_count:
                max_pudding_count = player.get_pudding()
                max_pudding_player = player

        max_pudding_player.add_points(6)


    def line_break(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

playGame = PlayGame()



