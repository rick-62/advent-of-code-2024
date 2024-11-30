import os

def load_input(day):
    '''load pre-downloaded puzzle input for specified day'''

    return open(os.path.join('inputs', f'day{day:0>2}.txt'))
