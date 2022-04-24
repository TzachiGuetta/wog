import GuessGame
import MemoryGame
import CurrencyRouletteGame
import Score


def welcome(name: str):
    return str(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")


def load_game():
    print(
        "Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you have toguess it back\n2. Guess Game - guess a number and see if you chose like the computer\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    chosen_game = input()
    if chosen_game not in ("1", "2", "3"):
        print("game number must be 1-3")
        exit()

    print("Please choose game difficulty from 1 to 5:")
    game_difficulty = int(input())
    if game_difficulty not in (1, 2, 3, 4, 5):
        print("game difficulty must be 1-5")
        exit()

    if chosen_game == "1":
        if MemoryGame.play(game_difficulty) == True:
            Score.add_score(game_difficulty)
    elif chosen_game == "2":
        if GuessGame.play(game_difficulty) == True:
            Score.add_score(game_difficulty)
    else:
        if CurrencyRouletteGame.play(game_difficulty) == True:
            Score.add_score(game_difficulty)
