from helper import load_input
import uuid

def parse_input_to_dict(input_string):
    numbers = [int(x) for x in input_string.split()]
    result_dict = {}
    previous_uuid = None

    for number in numbers:
        current_uuid = uuid.uuid4()
        if previous_uuid is not None:
            result_dict[previous_uuid] = (result_dict[previous_uuid][0], current_uuid)
        result_dict[current_uuid] = (number, None)
        previous_uuid = current_uuid

    return result_dict

def apply_rules(number):
    if number == 0:
        return 1
    elif len(str(number)) % 2 == 0:
        str_number = str(number)
        mid = len(str_number) // 2
        first_half = int(str_number[:mid])
        second_half = int(str_number[mid:])
        return first_half, second_half
    else:
        return number * 2024

def part1(contents, blinks=25):
    stones_dct = parse_input_to_dict(contents)
    for i in range(blinks):
        for current_uuid, (number, next_uuid) in list(stones_dct.items()):
            new_number = apply_rules(number)
            if type(new_number) == int:
                stones_dct[current_uuid] = (new_number, next_uuid)
            else:
                new_uuid = uuid.uuid4()
                stones_dct[current_uuid] = (new_number[0], new_uuid)
                stones_dct[new_uuid] = (new_number[1], next_uuid)       
    return len(stones_dct)
    

def part2(contents):
    pass

if __name__ == "__main__":

    test_input = load_input("day11_test").read()
    test_solution = part1(test_input)
    assert test_solution == 55312, test_solution
    test_solution = part2(test_input)
    assert test_solution == None, test_solution

    puzzle_input = load_input("day11").read()
    puzzle_solution = part1(puzzle_input)
    print(f"Part1: {puzzle_solution}")
    puzzle_solution = part2(puzzle_input)
    print(f"Part2: {puzzle_solution}")
