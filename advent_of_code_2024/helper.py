import os
import time

def load_input(filename):
    '''load puzzle or test input for specified filename'''

    return open(os.path.join('inputs', f'{filename}.txt'))

def print_map(puzzle_map, wait=0.1):
    os.system('clear')  # For Linux/OS X
    for row in puzzle_map:
        print(''.join(row))
    time.sleep(wait)