from controller import Controller
from model import Deck
from view import View

def main():
    deck = Deck()
    view = View()
    game = Controller(deck, view)
    game.run()

if __name__ == "__main__":
    main()