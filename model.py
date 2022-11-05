import random

SUITS = ("spade", "club", "heart", "diamond")
RANKS = (
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "jack",
    "queen",
    "king",
    "ace",
)

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.is_face_up = False

        self._rank_score = RANKS.index(self.rank)
        self._suit_score = SUITS.index(self.suit)

    # often used for printing the object 
    def __str__(self) -> str:
        return f"{self.suit} {self.rank} "

    # often used to get detailed information about the object   
    def __repr__(self) -> str:
        return str(self)
    
    # Use function to compare inferiority 
    def __lt__(self, other: "Card"):
        if self._rank_score != other._rank_score:
            return self._rank_score < other._rank_score
        
        return self._suit_score < other._suit_score

# inherit the list object
class Deck(list):
    def __init__(self):
        for rank in RANKS:
            for suit in SUITS:
                card = Card(suit, rank)
                self.append(card)
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self)
    
    # Same as list.pop(), but with more acurate name
    def draw_card(self):
        try:
            return self.pop()
        except IndexError:
            return None 

class Hand(list):
    def append(self, object):
        if not isinstance(object, Card):
            return ValueError("You can only add cards to your hand!")
        return super().append(object)

class Player():
    def __init__(self, name) -> None:
        self.name = name
        self.hand = Hand()
