import os
import time
import numpy as np
from helper import load_input

# input: map of the warehouse and a list of movements the robot will attempt to make
# The problem is that the movements will sometimes fail as boxes are shifted around
# As robot (@) attempts to move, if there are any boxes (O) in the way, the robot will also attempt to push those boxes
# if this action would cause the robot or a box to move into a wall (#), nothing moves
# The rest of the document describes the moves (^ for up, v for down, < for left, > for right)
# Afterwards get GPS coordinate of all boxes: 100 * distance from the top edge + distance from the left edge
# And finally sum these together for the answer

movement_vectors = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

def parse_input(input_text):
    # Split the input into map and directions
    map_part, directions_part = input_text.strip().split('\n\n', 1)
    
    # Parse the map into a 2D NumPy array
    map_lines = map_part.split('\n')
    map_2d_array = np.array([list(line) for line in map_lines])
    
    # Parse the directions into a list
    directions_lines = directions_part.split('\n')
    directions = [direction for line in directions_lines for direction in line]
    
    return map_2d_array, directions


def move(puzzle_map, original_position, direction):
    
    # Get the movement vector for the given direction
    movement = movement_vectors[direction]

    content = puzzle_map[original_position]
    
    # Calculate the new position of the robot
    new_position = (original_position[0] + movement[0], original_position[1] + movement[1])
    
    # Check if the new position is within bounds
    if (0 <= new_position[0] < puzzle_map.shape[0] and
        0 <= new_position[1] < puzzle_map.shape[1]):
        
        # Check the content of the new position
        new_position_content = puzzle_map[new_position]
        
        if new_position_content == '.':
            # Move to the new position
            puzzle_map[original_position] = '.'
            puzzle_map[new_position] = content
            pass
        
        elif new_position_content == 'O':
            # Calculate the new position of the box
            move(puzzle_map, new_position, direction)
        
            if puzzle_map[new_position] == '.':
                # Move the box and the robot
                puzzle_map[original_position] = '.'
                puzzle_map[new_position] = content
                pass


def print_map(puzzle_map, wait=0.1):
    os.system('clear')  # For Linux/OS X
    for row in puzzle_map:
        print(''.join(row))
    time.sleep(wait)

def part1(contents):
    puzzle_map, directions = parse_input(contents)
    for direction in directions:
        robot = tuple(np.argwhere(puzzle_map == '@')[0])
        move(puzzle_map, robot, direction)
        # print_map(puzzle_map, wait=0.1)

    # Find the coordinates of all boxes 'O'
    box_positions = np.argwhere(puzzle_map == 'O')
    
    # Calculate the sum of the GPS coordinates of all boxes
    total_sum = sum(100 * pos[0] + pos[1] for pos in box_positions)
    
    return total_sum


def parse_input_part2(input_text):
    # Split the input into map and directions
    map_part, directions_part = input_text.strip().split('\n\n', 1)
    
    # Parse the map into a 2D NumPy array with the specified transformations
    map_lines = map_part.split('\n')
    transformed_map_lines = []
    
    for line in map_lines:
        transformed_line = []
        for char in line:
            if char == '#':
                transformed_line.append('##')
            elif char == 'O':
                transformed_line.append('[]')
            elif char == '.':
                transformed_line.append('..')
            elif char == '@':
                transformed_line.append('@.')
        transformed_map_lines.append(''.join(transformed_line))
    
    # Convert the transformed lines into a 2D NumPy array
    transformed_map_2d_array = np.array([list(line) for line in transformed_map_lines])
    
    # Parse the directions into a list
    directions_lines = directions_part.split('\n')
    directions = [direction for line in directions_lines for direction in line]
    
    return transformed_map_2d_array, directions

def move_part2(puzzle_map, original_position, direction):
    
    # Get the movement vector for the given direction
    movement = movement_vectors[direction]

    content = puzzle_map[original_position]
    
    # Calculate the new position of the robot
    new_position = (original_position[0] + movement[0], original_position[1] + movement[1])
    
    # Check if the new position is within bounds
    if (0 <= new_position[0] < puzzle_map.shape[0] and
        0 <= new_position[1] < puzzle_map.shape[1]):
        
        # Check the content of the new position
        new_position_content = puzzle_map[new_position]
        
        if new_position_content == '.':
            # Move to the new position
            puzzle_map[original_position] = '.'
            puzzle_map[new_position] = content
            pass
        
        elif new_position_content == ']' or new_position_content == '[':
            # Calculate the new position of the box
            move_part2(puzzle_map, new_position, direction)
        
            if puzzle_map[new_position] == '.':
                # Move the box and the robot
                puzzle_map[original_position] = '.'
                puzzle_map[new_position] = content
                pass

def part2(contents):
    puzzle_map, directions = parse_input_part2(contents)
    print_map(puzzle_map, wait=0.1)
    for direction in directions:
        robot = tuple(np.argwhere(puzzle_map == '@')[0])
        move_part2(puzzle_map, robot, direction)
        print_map(puzzle_map, wait=1)


if __name__ == "__main__":

    test_input = load_input("day15_test").read()
    test_solution = part1(test_input)
    assert test_solution == 2028, test_solution

    test_input = load_input("day15_test2").read()
    test_solution = part1(test_input)
    assert test_solution == 10092, test_solution
    test_solution = part2(test_input)
    assert test_solution == 9021, test_solution


    puzzle_input = load_input("day15").read()
    puzzle_solution = part1(puzzle_input)
    print(f"Part1: {puzzle_solution}")
    puzzle_solution = part2(puzzle_input)
    print(f"Part2: {puzzle_solution}")
