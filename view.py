class View:
    def prompt_for_player(self):
        name = input("Name of player: ")
        if not name:
            return None
        return name

    def show_player_hand(self, name, hand):
        print(f"[Player {name}] ")
        for card in hand:
            if card.is_face_up:
                print(card)
            else:
                print("(Card face down)")

    def prompt_for_flip_cards(self):
        print()
        input("Ready to flip cards ?")
        return True
    
    def show_winner(self, name):
        print(f"{name} won! Congrats!")
    
    def prompt_for_new_game(self):
        print("Start a new game ?")
        choice = input("Y/n: ")
        if choice == "n":
            return False
        return True