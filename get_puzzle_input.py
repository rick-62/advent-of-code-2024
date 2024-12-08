import os
import shutil
import sys
from datetime import datetime

import requests


def create_script(day, directory='advent_of_code_2024'):
    '''create blank text file to be used for testing'''

    template_file = f"{directory}/template.py"
    new_file = f'{directory}/day{day:0>2}.py'

    if not os.path.exists(new_file): 
        shutil.copyfile(template_file, new_file)
        print(f"File copied from {template_file} to {new_file}") 
    else: 
        print(f"{new_file} already exists. No copy was made.")


def create_blank_test_file(day):
    '''create blank text file to be used for testing'''

    file_path = f'inputs/day{day:0>2}_test.txt'

    if os.path.exists(file_path): 
        print("Test file already exists. Will not overwrite!") 
    else: 
        with open(file_path, 'w') as f:
            pass
        print(f"Blank test file created in {file_path}")


def download_puzzle_input(day, year=2024):
    '''download the users puzzle input from Advent of Code site'''

    session = os.getenv('aoc_session')
    assert session != None

    cookies = {'session': session}

    r = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies=cookies)

    r.raise_for_status()
    print("Puzzle input downloaded successfully.")

    return r


def save_puzzle_input(text, day):
    '''save puzzle input as text file'''

    file_path = f"inputs/day{day:0>2}.txt"

    with open(file_path, 'w') as f:
        f.write(text)

    print(f"Puzzle input saved to {file_path}.")
    

def get_day_of_month():

    # Get the current date and time
    now = datetime.now()

    # Extract the day of the month
    current_day = now.day

    return current_day


if __name__ == '__main__':

    try:
        day = int(sys.argv[1])
    except:
        day = get_day_of_month()

    create_blank_test_file(day)
    create_script(day)
    r = download_puzzle_input(day)
    save_puzzle_input(r.text, day)