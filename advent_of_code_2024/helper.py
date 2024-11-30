import os

def load_input(filename):
    '''load puzzle or test input for specified filename'''

    return open(os.path.join('inputs', f'{filename}.txt'))
