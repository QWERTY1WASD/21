import os
from random import shuffle
from functions import *


console_clear = lambda: os.system('cls')


### DECK OF CARDS ###
deck_of_cards = {
    "Ace": 11,
    "Jack": 2,
    "Queen": 3,
    "King": 4,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
}

### RULES ###
change_the_price_of_an_ace_when_going_through = True
golden_ace = True
five_identical_pictures = True


def single_game():
    cards = [card for card in deck_of_cards.keys()]
    shuffle(cards)
    player_cards = list()
    player_score = 0
    print_player_deck(cards)  # TO DELETE
    while True:
        card = cards.pop()
        player_cards.append(card)
        player_score += deck_of_cards.get(card, 0)
        print(f"Вы ватащили {card}")
        print(f"Счёт: {player_score}")
        print_player_deck(player_cards)
        input()


def main():
    print("""
    
    РЕЖИМЫ
1 - you VS __NONE__ (single game)
2 - you VS bot
3 - you VS human

""")
    print("Выберите режим >>> ")
    console_clear()
    single_game()


if __name__ == "__main__":
    print("Добро пожаловать")
    main()
    #print("До встречи")
