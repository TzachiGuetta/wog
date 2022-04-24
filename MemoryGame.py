import random, sys, time


def generate_sequence(difficulty):
    random_numbers = []
    for i in range(0, int(difficulty)):
        n = random.randint(1, 30)
        random_numbers.append(n)
    return random_numbers


def get_list_from_user(list_length):
    user_list = []
    for i in range(0, list_length):
        n = input()
        user_list.append(int(n))
    return user_list


def is_list_equal(user_list, random_numbers):
    if user_list == random_numbers:
        return True
    return False

def play(difficulty):
    rand = generate_sequence(difficulty)
    print(rand)
    # Remove the line after 0.7 sec
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    time.sleep(0.7)
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)
    usr = get_list_from_user(difficulty)
    print(usr)
    return is_list_equal(usr, rand)