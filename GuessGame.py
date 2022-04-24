from random import random, randint


def generate_number():
    return randint(1, 5)


def get_guess_from_user():
    print("Please choose game  difficulty from 1 to 5:")
    difficulty = input()
    if difficulty not in ("1", "2", "3", "4", "5"):
        print("game difficulty must be 1-5")
    return difficulty


def compare_results(difficulty, secret_number):
    if secret_number == int(difficulty):
        print(f"secret_number == difficulty \n secret_number = {secret_number}, difficulty = {difficulty}")
        return True
    print(f"secret_number != difficulty, \n secret_number = {secret_number}, difficulty = {difficulty}")
    return False


def play(difficulty: str):
    secret_number = generate_number()
    if difficulty == "":
        difficulty = get_guess_from_user()
    return compare_results(difficulty, secret_number)
