import requests
import os
import sys


def download_puzzle_input(day, year=2023):
    '''download the users puzzle input from Advent of Code site'''

    session = os.getenv('aoc_session')
    print(session)
    assert session != None

    cookies = {'session': session}

    r = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies=cookies)

    r.raise_for_status()

    return r


def save_puzzle_input(text, day):
    '''save puzzle input as text file'''

    with open(f'inputs/day{day:0>2}.txt', 'w') as f:
        f.write(text)
    

if __name__ == '__main__':

    day = int(sys.argv[1])
    r = download_puzzle_input(day)
    save_puzzle_input(r.text, day)