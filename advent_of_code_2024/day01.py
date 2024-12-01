from helper import load_input

def part1(contents):
    # Read all lines and split into columns
    lines = contents.readlines()
    list1 = []
    list2 = []

    for line in lines:
        numbers = list(map(int, line.split()))
        list1.append(numbers[0])
        list2.append(numbers[1])

    # Sort both lists
    list1.sort()
    list2.sort()

    # Subtract corresponding elements and sum the results
    result = sum(abs(a - b) for a, b in zip(list1, list2))

    return result



if __name__ == "__main__":
    test_input = load_input('day01_test')
    test_solution = part1(test_input)
    assert test_solution== 11, test_solution

    puzzle_input = load_input('day01')
    puzzle_solution = part1(puzzle_input)
    print(puzzle_solution)