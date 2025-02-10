class Card:

    def __init__(self, value: str, suit: str):

        self.value = value

        self.suit = suit

    def __repr__(self):

        return f"{self.value} of {self.suit}"


class Hand:

    """The hand in a poker game."""


    suits = ["diamonds", "clubs", "hearts", "spades"]

    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    values_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14}


    def __init__(self):

        """Initialize Hand."""

        self.cards = []


    def can_add_card(self, card: Card) -> bool:

        """

        Check for card validity.


        Can only add card if:

        - A card with the same suit and value is already not being held.

        - The player is holding less than five cards

        - The card has both a valid value and a valid suite.

        """

        control = False

        if any([card_in_hand.value == card.value and card_in_hand.suit == card.suit for card_in_hand in self.cards]):

            control = False

        else:

            if len(self.cards) < 5:

                if card.value in self.values and card.suit in self.suits:

                    control =  True

        return control


    def add_card(self, card: Card):

        """

        Add a card to hand.


        Before adding a card, you would have to check if it can be added.

        """

        if self.can_add_card(card):

            self.cards.append(card)


    def can_remove_card(self, card: Card):

        """

        Check if a card can be removed from hand.


        The only consideration should be that the card is already being held.

        """

        for card_in_hand in self.cards:

            if card_in_hand.value == card.value and card_in_hand.suit == card.suit:

                return True

        return False


    def remove_card(self, card: Card):

        """

        Remove a card from hand.


        Before removing the card, you would have to check if it can be removed.

        """

        if self.can_remove_card(card):

            self.cards.remove(card)


    def get_cards(self):

        """Return a list of cards as objects."""

        return self.cards


    def is_straight(self):

        """

        Determine if the hand is a straight.


        A straight hand will have all cards in the order of value.

        Sorting will help you here as the order will vary.


        Examples:

        4 5 6 7 8

        K J 10 Q A



        For the sake of simplicity - A 2 3 4 5 will not be tested.

        You can always consider A to be the highest ranked card.

        """

        cards = self.get_cards()

        for card in cards:

            if card.value in self.values_dict.keys():

                card.value = self.values_dict[card.value]

        cards = sorted(cards, key=lambda card: card.value)

        control = False

        for i in range(len(cards)-1):

            if cards[i].value + 1 == cards[i+1].value:

                control = True

            else:

                return False

        return control


    def is_flush(self):

        """

        Determine if the hand is a flush.


        In a flush hand all cards are the same suit. Their number value is not important here.

        """

        cards = self.get_cards()

        control = False

        for i in range(len(cards) - 1):

            if cards[i].suit == cards[i + 1].suit:

                control = True

            else:

                return False

        return control



    def is_straight_flush(self):

        """

        Determine if the hand is a straight flush.


        Such a hand is both straight and flush at the same time.


        """

        if self.is_straight() and self.is_flush():

            return True

        else:

            return False


    def is_full_house(self):

        """

        Determine if the hand is a full house.


        A house will have three cards of one value, and two cards of a second value.

        For example:

        2 2 2 6 6

        K J K J K

        """

        cards = self.get_cards()

        counter = {}

        for card in cards:

            if card.value not in counter:

                counter[card.value] = 0

            counter[card.value] += 1

        if len(counter) == 2 and set(counter.values()) == set([2, 3]):

            return True

        else:

            return False


    def is_four_of_a_kind(self):

        """

        Determine if there are four cards of the same value in hand.


        For example:

        2 2 K 2 2

        9 4 4 4 4


        """

        cards = self.get_cards()

        counter = {}

        for card in cards:

            if card.value not in counter:

                counter[card.value] = 0

            counter[card.value] += 1

        if len(counter) == 2 and set(counter.values()) == set([1, 4]):

            return True

        else:

            return False


    def is_three_of_a_kind(self):

        """

        Determine if there are three cards of the same value in hand.


        For Example:

        Q 4 Q Q 7

        5 5 1 5 2


        """

        cards = self.get_cards()

        counter = {}

        for card in cards:

            if card.value not in counter:

                counter[card.value] = 0

            counter[card.value] += 1

        if len(counter) == 3 and 3 in counter.values():

            return True

        else:

            return False


    def is_pair(self):

        """

        Determine if there are two kinds of the same value in hand.


        For example:

        5 A 2 K A

        8 7 6 6 5


        """

        cards = self.get_cards()

        counter = {}

        for card in cards:

            if card.value not in counter:

                counter[card.value] = 0

            counter[card.value] += 1

        if 2 in counter.values():

            return True

        else:

            return False


    def get_hand_type(self):

        """

        Return a string representation of the hand.


        Return None (or nothing), if there are less than five cards in hand.


        "straight flush" - Both a straight and a flush

        "flush" - The cards are all of the same suit

        "straight" - The cards can be ordered

        "full house" - Three cards are of the same value while the other two also share a value.

        "four of a kind" - Four cards are of the same value

        "three of a kind" - Three cards are of the same value

        "pair" - Two cards are of the same value

        "high card" - None of the above


        """

        if len(self.cards) < 5:

            return None

        else:

            if self.is_straight() and self.is_flush():

                return 'straight flush'

            elif self.is_flush():

                return 'flush'

            elif self.is_straight():

                return 'straight'

            elif self.is_full_house():

                return 'full house'

            elif self.is_four_of_a_kind():

                return 'four of a kind'

            elif self.is_three_of_a_kind():

                return 'three of a kind'

            elif self.is_pair():

                return 'pair'

            else:

                return 'high card'


    def __repr__(self):

        """

        Return a string representation of the hand.


        I got a {type} with cards: {card list}

        I got a straight with cards: 2 of diamonds, 4 of spades, 5 of clubs, 3 of diamonds, 6 of hearts


        If a hand type cannot be yet determined, return a list of cards as so:


        I'm holding {cards}

        I'm holding 2 of diamonds, 4 of spades.


        Order of the cards is not important.

        """

        if self.get_hand_type() == None:

            return f"I'm holding {self.cards}"

        else:

            return f"I got a {self.get_hand_type()} with cards: {self.cards}"