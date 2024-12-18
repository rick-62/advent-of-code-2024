from helper import load_input
import numpy as np
import os

def create_2D_array(shape):
    array = np.full(shape, ".", dtype=str)
    return array

def print_2D_array(array, particles):
    os.system('clear')  # For Linux/OS X
    array.fill(".") 
    for particle in particles:
        x, y = particle.position
        if array[x, y] == ".":  # If the position is not already occupied
            array[x, y] = "1"
        else:
            array[x, y] = str(int(array[x, y]) + 1)
    for row in array.T:
        print("".join(row), flush=True)

def update_2D_array(array, particles):
    array.fill(".") 
    for particle in particles:
        x, y = particle.position
        if array[x, y] == ".":  # If the position is not already occupied
            array[x, y] = "1"
        else:
            array[x, y] = str(int(array[x, y]) + 1)
    return array

class Particle:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def __repr__(self):
        return f"Particle(position={self.position}, velocity={self.velocity})"


def parse_input(input_str):
    particles = []
    lines = input_str.strip().split('\n')
    for line in lines:
        parts = line.split()
        p = tuple(map(int, parts[0][2:].split(',')))
        v = tuple(map(int, parts[1][2:].split(',')))
        particles.append(Particle(p, v))
    return particles

def replace_middle_row_and_column(array):
    rows, cols = array.shape
    mid_row = rows // 2
    mid_col = cols // 2

    # Replace the middle row with "."
    array[mid_row, :] = "."
    # Replace the middle column with "."
    array[:, mid_col] = "."

    return array

def sum_quadrants(array):
    rows, cols = array.shape
    mid_row = rows // 2
    mid_col = cols // 2

    # Define the four quadrants
    q1 = array[:mid_row, :mid_col]
    q2 = array[:mid_row, mid_col+1:]
    q3 = array[mid_row+1:, :mid_col]
    q4 = array[mid_row+1:, mid_col+1:]

    # Convert elements to integers where possible and sum
    def sum_quadrant(quadrant):
        return np.sum([int(x) for row in quadrant for x in row if x.isdigit()])

    sum_q1 = sum_quadrant(q1)
    sum_q2 = sum_quadrant(q2)
    sum_q3 = sum_quadrant(q3)
    sum_q4 = sum_quadrant(q4)

    return sum_q1, sum_q2, sum_q3, sum_q4

def part1(contents, iterations=100, shape=(101, 103)):
    particles = parse_input(contents)
    array = create_2D_array(shape)
    print_2D_array(array, particles)
    print("Iteration: 0")
    for i in range(iterations):
        for particle in particles:
            x, y = particle.position
            dx, dy = particle.velocity
            # Update position and wrap around using modulo operator
            new_x = (x + dx) % shape[0]
            new_y = (y + dy) % shape[1]
            particle.position = (new_x, new_y)
        print_2D_array(array, particles)
        print(f"Iteration: {i+1}")
    
    array = replace_middle_row_and_column(array)
    sum_q1, sum_q2, sum_q3, sum_q4 = sum_quadrants(array)
    result = sum_q1 * sum_q2 * sum_q3 * sum_q4
    return int(result)


def check_vertical_symmetry(array):
    rows, cols = array.shape
    mid_col = cols // 2

    # Define the four quadrants
    h1 = array[:, :mid_col]
    h2 = array[:, mid_col+1:]
    
    # Check if the left half is the mirror image of the right half
    
    return np.array_equal(h1, np.fliplr(h2))

def check_all_ones(array):
    ones = [int(x) for row in array for x in row if x.isdigit()]
    return all(x == 1 for x in ones)


def part2(contents, shape=(101, 103)):
    particles = parse_input(contents)
    array = create_2D_array(shape)
    i = 0
    while True:
        i += 1
        for particle in particles:
            x, y = particle.position
            dx, dy = particle.velocity
            # Update position and wrap around using modulo operator
            new_x = (x + dx) % shape[0]
            new_y = (y + dy) % shape[1]
            particle.position = (new_x, new_y)
        update_2D_array(array, particles)

        if check_all_ones(array):
            return i
    


if __name__ == "__main__":

    test_input = load_input("day14_test").read()
    test_solution = part1(test_input, shape=(11, 7))
    assert test_solution == 12, test_solution
    # test_solution = part2(test_input)
    # assert test_solution == None, test_solution

    puzzle_input = load_input("day14").read()
    puzzle_solution = part1(puzzle_input)
    print(f"Part1: {puzzle_solution}")
    puzzle_solution = part2(puzzle_input)
    print(f"Part2: {puzzle_solution}")
