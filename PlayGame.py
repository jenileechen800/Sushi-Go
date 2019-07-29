from src.Player import Player
from Cards.GameDeck import GameDeck


class PlayGame:
    def __init__(self):
        self.players = []
        self.players_iterator = None
        self.text_introduction()
        self.game_deck = GameDeck(len(self.players))

        self.play_game()

    def play_game(self):
        self.play_rounds()
        self.total_points()
        self.print_winners()

    def play_rounds(self):
        self.players_iterator = self.players.__iter__()
        for mini_deck in self.game_deck.game_deck:
            while len(mini_deck.deck) > 0:
                try:
                    curr_player = self.players_iterator.__next__()
                    self.pick_card(curr_player, mini_deck)
                except StopIteration:
                    self.players_iterator = self.players.__iter__()

    def pick_card(self, player, mini_deck):
        self.line_break()
        print("Minideck " + str(mini_deck.name) + ": " + str(self.show_deck(mini_deck.deck)))

        selected_card = input("\n\n\"" + player.name + "\" please type selected card: \n").lower()

        while not self.card_in_deck(player, selected_card, mini_deck.deck):
            self.line_break()
            print(self.show_deck(mini_deck.deck))
            print("This card was not found in the card deck, please try again\n")
            selected_card = input("Please type selected card: \n").lower()

    def card_in_deck(self, player, selected_card, mini_deck):
        for card in mini_deck:
            if selected_card.lower() == card.name.lower():
                player.add_card(card)
                mini_deck.remove(card)

                print("\"" + selected_card + "\" added to " + player.name + "\'s deck")

                # if selected_card.lower() == "chopsticks":
                #     self.pick_card(player, mini_deck)
                #     self.pick_card(player, mini_deck)
                return True

        return False

    def show_deck(self, mini_deck):
        card_names = []
        for card in mini_deck:
            card_names.append(card.name)

        return card_names

    def text_introduction(self):
        self.line_break()
        print("Welcome to SushiGo:).")
        self.instructions()

        self.line_break()

        accept_num_players = False

        while not accept_num_players:
            num_players = int(input("Please enter the # of players (2-5 players)\n"))

            if 5 >= num_players >= 2:
                accept_num_players = True
            else:
                print("That is not an acceptable number of players")

        self.line_break()
        for player in range(int(num_players)):
            player = Player(input("Please enter \"Player" + str(player) + "\" name:\n"))
            self.players.append(player)

    def instructions(self):
        read_instructions = input("Would you like to read the instructions? (y/n)\n")

        if read_instructions == "y":
            self.line_break()
            print("The game takes place over 3 rounds. \n"
                  "To start a round, all players simultaneously"
                  "choose any 1 card from their hands that they would\n"
                  "like to keep and place it face-down in front of them.\n"
                  "When each player has done this, everyone reveals their chosen cards.\n"
                  "After revealing cards, pass your remaining hand face-down\n"
                  "to the player on your left. Everyone picks up their new hands\n "
                  "and the next turn begins. You now have a new and smaller hand to choose from.\n")

    def total_points(self):
        self.maki_points()
        self.pudding_points()

        for player in self.players:
            player.total_points()

        # sort 'players' list from largest to smallest

    def print_winners(self):
        self.line_break()
        print("And the winners are...by max number of points: ")
        count = 1

        sorted_players_list = self.sorted_players_list()
        for player in sorted_players_list:
            print(str(count) + ". " + str(player.name) + " (" + str(player.points) + " points)")
            count += 1

    def sorted_players_list(self):
        sorted_players_list = []

        player_points = []
        for player in self.players:
            player_points.append(player.points)
        player_points.sort(reverse=True)

        for player in self.players:
            for point_amt in player_points:
                if player.points == point_amt and not sorted_players_list.__contains__(player):
                    sorted_players_list.append(player)

        return sorted_players_list

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
