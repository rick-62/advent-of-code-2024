from helper import load_input
from itertools import zip_longest
import numpy as np

def parse_input(contents):
    contents = contents.strip("\n")

    list1 = contents[::2]
    blocks = []
    for i, n in enumerate(list1):
        block = [i] * int(n)
        blocks.append(block)
    
    list2 = [int(x) for x in contents[1::2]]
    spaces = []
    for n in list2:
        space = n * ['.']
        spaces.append(space)

    interweaved = [val for pair in zip_longest(blocks, spaces, fillvalue=[]) for val in pair]
    return np.concatenate(interweaved)


def part1(contents):
    disk = parse_input(contents)

    mask = disk != '.'
    block_indicies = list(np.where(mask)[0])
    for index in range(len(disk)):
        if index > block_indicies[-1]:
            break
        if disk[index] == '.':
            rightmost_block_index = block_indicies.pop()
            disk[index] = disk[rightmost_block_index]
            disk[rightmost_block_index] = '.'

    return sum([i*int(n) for i, n in enumerate(disk) if n != '.'])
        

def part2(contents):
    disk = parse_input(contents)
    # Add your logic here
    pass

if __name__ == "__main__":
    test_input = load_input("day09_test").read()
    test_solution = part1(test_input)
    assert test_solution == 1928, test_solution
    test_solution = part2(test_input)
    assert test_solution == None, test_solution

    puzzle_input = load_input("day09").read()
    puzzle_solution = part1(puzzle_input)
    print(f"Part1: {puzzle_solution}")
    puzzle_solution = part2(puzzle_input)
    print(f"Part2: {puzzle_solution}")
