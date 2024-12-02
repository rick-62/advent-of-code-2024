import numpy as np
from helper import load_input

def is_safe(row):
    increasing = all(row[i] < row[i+1] and row[i+1] - row[i] <= 3 for i in range(len(row) - 1))
    decreasing = all(row[i] > row[i+1] and row[i] - row[i+1] <= 3 for i in range(len(row) - 1))
    return increasing or decreasing

def part1(contents):
    # Load the input data
    data = contents.read()

    # Split the data into rows
    rows = data.strip().split('\n')

    # Split each row into individual numbers and convert to integers
    list_of_lists = [list(map(int, row.split())) for row in rows]

    # Determine if each row is safe
    safe_rows = [is_safe(row) for row in list_of_lists]

    return sum(safe_rows)

def part2(contents):
    # Load the input data
    data = contents.read()

    # Split the data into rows
    rows = data.strip().split('\n')

    # Split each row into individual numbers and convert to integers
    list_of_lists = [list(map(int, row.split())) for row in rows]

    # Determine if each row is safe or can be made safe by removing one integer
    safe_rows = []
    for row in list_of_lists:
        if is_safe(row):
            safe_rows.append(True)
        else:
            # Try removing each integer one by one
            row_safe = False
            for i in range(len(row)):
                new_row = row[:i] + row[i+1:]
                if is_safe(new_row):
                    row_safe = True
                    break
            safe_rows.append(row_safe)

    return sum(safe_rows)

if __name__ == "__main__":
    test_input = load_input('day02_test')
    test_solution_part1 = part1(test_input)
    assert test_solution_part1 == 2, test_solution_part1
    
    test_input = load_input('day02_test')
    test_solution_part2 = part2(test_input)
    assert test_solution_part2 == 4, test_solution_part2
    
    puzzle_input = load_input('day02')
    print(part1(puzzle_input))

    puzzle_input = load_input('day02')
    print(part2(puzzle_input))
