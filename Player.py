from Cards.Card import Card


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.points = 0
        self.last_card = Card("blank")
        self.points_dict = {}

    def add_card(self, card):
        self.cards.append(card)
        self.wasabi_nigiri(card)
        # self.chopsticks(card)

    def wasabi_nigiri(self, card):
        last_card = self.last_card.name
        current_card = getattr(card, "name")
        wasabi_nigiri_pair = []

        if current_card == "Wasabi":
            if last_card == "Salmon Nigiri" or last_card == "Squid Nigiri" or last_card == "Egg Nigiri":
                wasabi_nigiri_pair.append(current_card, last_card)
                self.cards.remove(current_card)
                self.cards.remove(last_card)
                self.cards.append(wasabi_nigiri_pair)

    def chopsticks(self, card):
        if card.name == "Chopsticks":
            self.show_cards()
            removed_cards_list = input(
                "Please type name of 2 cards you would like to exchange: (comma-separated)").strip().split(",")

        for removed_card in removed_cards_list:
            while not (contains_cards(removed_card)):
                print(removed_card + " does not seem to be in your current cards list")

            self.cards.remove(removed_card)

    def contains_cards(self, removed_card):
        for card in self.cards:
            if card.name == removed_card:
                return True
        return False

    def show_cards(self):
        card_names = []
        for card in self.cards:
            card_names.append(card.name)
        print(card_names)

    def total_points(self):
        self.nigiri_points()
        self.tempura_points()
        self.sashimi_points()
        self.dumpling_points()
        self.wasabi_points()
        self.points_track_record()

    def nigiri_points(self):
        nigiri_points = 0
        for card in self.cards:
            if card.name == "Squid Nigiri":
                nigiri_points += 3

            elif card.name == "Salmon Nigiri":
                nigiri_points += 2

            elif card.name == "Egg Nigiri":
                nigiri_points += 1

        self.points_dict["Nigiri Points"] = nigiri_points
        self.points += nigiri_points

    def tempura_points(self):
        total_tempura = 0

        for card in self.cards:
            if card.name == "Tempura":
                total_tempura += 1

        tempura_points = total_tempura / 2
        self.points_dict["Tempura Points"] = tempura_points
        self.points = tempura_points

    def sashimi_points(self):
        total_sashimi = 0

        for card in self.cards:
            if card.name == "Sashimi":
                total_sashimi += 1

        sashimi_points = total_sashimi / 3
        self.points_dict["Tempura Points"] = sashimi_points
        self.points = sashimi_points

    def dumpling_points(self):
        dumpling_points = 0
        total_dumplings = 0

        for card in self.cards:
            if card.name == "Dumpling":
                total_dumplings += 1

        if total_dumplings == 1:
            dumpling_points += 1
        elif total_dumplings == 2:
            dumpling_points += 3
        elif total_dumplings == 3:
            dumpling_points += 6
        elif total_dumplings == 4:
            dumpling_points += 10
        elif total_dumplings >= 5:
            dumpling_points += 15

        self.points_dict["Dumpling Points"] = dumpling_points
        self.points = dumpling_points

    def wasabi_points(self):
        wasabi_nigiri_points = 0

        for card in self.cards:
            if card.__class__ == list:
                wasabi_nigiri_points = card[1] * 3

        self.points += wasabi_nigiri_points
        self.points_dict["Wasabi-NigiriPoints"] = wasabi_nigiri_points

    def get_maki(self):
        total_maki = 0
        for card in self.cards:
            if card.name == "Maki(3)":
                total_maki += 3
            elif card.name == "Maki(2)":
                total_maki += 2
            elif card.name == "Maki(1)":
                total_maki += 1

        return total_maki

    def get_pudding(self):
        total_puddings = 0
        for card in self.cards:
            if card.name == "Pudding":
                total_puddings += 1

        return total_puddings

    def add_points(self, points):
        self.points += points

    def points_track_record(self):
        pass
        # self.line_break()
        # print("Points Track Record:")
        # for k, v in self.points_dict:
        #     print(k + ": " + v + " points")
        # self.line_break()

    def line_break(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



