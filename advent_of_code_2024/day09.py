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
        
def parse_input_part2(contents):
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

    return blocks, spaces

def part2(contents):
    blocks, spaces = parse_input_part2(contents)
    
    def move_element(lst, from_index, to_index):
        element = lst[from_index]
        lst[from_index] = []
        lst.insert(to_index, element)
        return lst


    for block in blocks.copy()[::-1]:
        i = blocks.index(block)
        for j, space in enumerate(spaces):
            if j > i:
                break
            remaining = len(space) - len(block)
            if remaining >= 0:
                blocks = move_element(blocks, i, j+1)
                spaces.insert(j, [])
                spaces[j+1] = spaces[j+1][:remaining]
                blocks.insert(i+1, [])
                spaces.insert(i+1, len(block) * ['.'])
                break

    interweaved = [val for pair in zip_longest(blocks, spaces, fillvalue=[]) for val in pair]
    disk = np.concatenate(interweaved)

    return sum([i*int(n) for i, n in enumerate(disk) if n != '.'])

if __name__ == "__main__":
    test_input = load_input("day09_test").read()
    test_solution = part1(test_input)
    assert test_solution == 1928, test_solution
    test_solution = part2(test_input)
    assert test_solution == 2858, test_solution

    puzzle_input = load_input("day09").read()
    puzzle_solution = part1(puzzle_input)
    print(f"Part1: {puzzle_solution}")
    puzzle_solution = part2(puzzle_input)
    print(f"Part2: {puzzle_solution}")
