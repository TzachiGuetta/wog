import requests
curr_value = -1

def get_money_interval(roulette_game_difficulty):
    # Where USD is the base currency you want to use
    url = 'https://v6.exchangerate-api.com/v6/af236e80e1d0644e39934436/latest/USD'
    global curr_value
    # Making our request
    response = requests.get(url)
    data = response.json()
    curr_value = data['conversion_rates']['ILS'].__round__(2)
    generated_interval = ((curr_value - (5 - roulette_game_difficulty)).__round__(2),
                          (curr_value + (5 - roulette_game_difficulty)).__round__(2))
    return generated_interval

def get_guess_from_user():
    print(f"guess of value to a given amount of USD")
    return float(input())

def play(difficulty):
    generated_interval = get_money_interval(difficulty)
    user_number_input = get_guess_from_user()
    if generated_interval[0] <= user_number_input <= generated_interval[1]:
        print(f'You WON! You guessed right, the exact current currency rate from USD to ILS is {curr_value}')
        return True
    print(f'You LOST! You have not guessed right, the exact current currency rate from USD to ILS is {curr_value}')
