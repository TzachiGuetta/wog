import os
from os import system, name

bad_return_code = 500
score_file_name = 'score.txt'
os.environ['TERM'] = 'xterm'


def Screen_cleaner():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
