# Deck of Cards Exercise
# implement two classes, Card and Deck
# Card:
    # each instance of card should have a suit, value and __repr__ shoudl display the cards value and suit

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    
    def __repr__(self):
        # pre-3.6 way -> return "{} of {}".format(self.value, self.suit)
        return f"{self.value} of {self.suit}"

# Deck:
#   Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
#   Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
#   Deck 's __repr__  method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
#   Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
#   Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should return a ValueError  with the message "Only full decks can be shuffled".  shuffle should return the shuffled deck.
#   Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck and return that single card.
#   Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck and return that list of cards.

class Deck: 
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] # leave all strings to avoid confusion
        # This is the non-Pythonic way:
        # self.cards = []
        # for suit in suits:
        #     for value in values:
        #         # print(Card(value, suit)) <- shows that this works
        #         self.cards.append(Card(value, suit))
        #This is the Pythonic way (list comprehension):
        self.cards = [Card(value, suit) for suit in suits for value in values]
        # print(self.cards) # <-- to test

    def __repr__(self):
        return f"Deck of {self.count()} cards" # use the count method you created here!  don't repeat tasks

    def count(self):
        return len(self.cards)

    def _deal(self, num_cards_remove):
        count = self.count()
        actual = min([count, num_cards_remove]) # Will remove 52 cards from a full deck
        if count == 0:
            raise ValueError("All cards have been dealt!")
        # print(f"Going to remove {actual} cards") # <-- to test
        # use slice syntax to remove cards from deck:
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards




d = Deck()  # Call an instance of the class Deck :-) 

print(d) # without __repr__ this gives you <__main__.Deck object at 0x00000232F1D31048>

print(d.count())

#d._deal(54) 

print(d._deal(3))
print(d.count())
