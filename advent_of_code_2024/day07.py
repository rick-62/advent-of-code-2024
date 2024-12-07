from helper import load_input
import itertools

def parse_input(data):
    parsed_data = []
    for line in data.strip().split('\n'):
        total, numbers = line.split(':')
        numbers_list = numbers.strip().split()
        parsed_data.append((int(total), numbers_list))
    return parsed_data

def part1(data):
    total = 0
    for value, numbers in parse_input(data):
        combinations = itertools.product('*+', repeat=len(numbers)-1)
        for comb in combinations:
            equation = '{}'.join(numbers).format(*comb)
            # Evaluate left-to-right manually
            calc = int(numbers[0])
            for i, op in enumerate(comb):
                if op == '+':
                    calc += int(numbers[i + 1])
                elif op == '*':
                    calc *= int(numbers[i + 1])
            if calc == value:
                total += value
                break
    return total


def part2(data):
    total = 0
    for value, numbers in parse_input(data):
        combinations = itertools.product('*+|', repeat=len(numbers)-1)
        for comb in combinations:
            # Evaluate left-to-right manually
            calc = int(numbers[0])
            for i, op in enumerate(comb):
                if op == '+':
                    calc += int(numbers[i + 1])
                elif op == '*':
                    calc *= int(numbers[i + 1])
                elif op == '|':
                    calc = int(str(calc) + str(numbers[i + 1]))
            if calc == value:
                total += value
                break
    return total

if __name__ == "__main__":
    test_input = load_input('day07_test').read()
    test_solution = part1(test_input)
    assert test_solution == 3749, f"Test failed, got {test_solution}"
    test_solution = part2(test_input)
    assert test_solution == 11387, f"Test failed, got {test_solution}"

    puzzle_input = load_input('day07').read()
    puzzle_solution = part1(puzzle_input)
    print(puzzle_solution)
    puzzle_solution = part2(puzzle_input)
    print(puzzle_solution)

