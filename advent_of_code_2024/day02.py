import numpy as np
from helper import load_input

def is_safe(row):
    """
    Check if a row is safe.
    A row is considered safe if it is strictly increasing or strictly decreasing,
    and no two adjacent numbers differ by more than 3.
    """
    increasing = all(row[i] < row[i+1] and row[i+1] - row[i] <= 3 for i in range(len(row) - 1))
    decreasing = all(row[i] > row[i+1] and row[i] - row[i+1] <= 3 for i in range(len(row) - 1))
    return increasing or decreasing

def part1(data):
    """
    Process the input data and count the number of safe rows.
    """
    # Split the data into rows
    rows = data.strip().split('\n')

    # Split each row into individual numbers and convert to integers
    list_of_lists = [list(map(int, row.split())) for row in rows]

    # Determine if each row is safe
    safe_rows = [is_safe(row) for row in list_of_lists]

    # Count the number of safe rows
    return sum(safe_rows)

def part2(data):
    """
    Process the input data and count the number of safe rows.
    A row is considered safe if it is safe as is, or if removing a single integer makes it safe.
    """
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

    # Count the number of safe rows
    return sum(safe_rows)

if __name__ == "__main__":
    test_input = load_input('day02_test').read()
    assert part1(test_input) == 2
    assert part2(test_input) == 4
    
    puzzle_input = load_input('day02').read()
    print(part1(puzzle_input))
    print(part2(puzzle_input))
