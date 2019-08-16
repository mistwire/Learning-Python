# Deck of Cards Exercise
# implement two classes, Card and Deck
# Card:
    # each instance of card should have a suit, value and __repr__ shoudl display the cards value and suit
# Deck:
#   Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
#   Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
#   Deck 's __repr__  method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
#   Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
#   Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should return a ValueError  with the message "Only full decks can be shuffled".  shuffle should return the shuffled deck.
#   Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck and return that single card.
#   Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck and return that list of cards.

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{value} of {suit}"

class Deck: 
    pass


