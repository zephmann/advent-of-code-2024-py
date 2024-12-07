import re

import advent


def parse_memory(memory_str: str) -> int:
    """Calculate the total of the multiplication instructions
    in the corrupted program memory.

    It seems like the goal of the program is just to multiply some numbers.
    It does that with instructions like mul(X,Y), where X and Y are each 1-3
    digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result
    of 2024. Similarly, mul(123,4) would multiply 123 by 4.

    However, because the program's memory has been corrupted, there are also
    many invalid characters that should be ignored, even if they look like
    part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34),
    or mul ( 2 , 4 ) do nothing.
    """
    # "mul(" + 1-3 digit as x + "," + 1-3 digit as y + ")"
    #  mul\(   (?P<x> \d{1,3})   ,    (?P<y> \d{1,3})  \)
    pattern = r"mul\((?P<x>\d{1,3}),(?P<y>\d{1,3})\)"

    total = 0
    for match in re.finditer(pattern, memory_str):
        total += int(match.group("x")) * int(match.group("y"))
    return total


def test_parse_memory():
    value = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert parse_memory(value) == 161


def parse_memory_with_enable(memory_str: str) -> int:
    """Calculate the total of the multiplication instructions
    in the corrupted program memory.

    It seems like the goal of the program is just to multiply some numbers.
    It does that with instructions like mul(X,Y), where X and Y are each 1-3
    digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result
    of 2024. Similarly, mul(123,4) would multiply 123 by 4.

    However, because the program's memory has been corrupted, there are also
    many invalid characters that should be ignored, even if they look like
    part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34),
    or mul ( 2 , 4 ) do nothing.
    """
    # same as above except also looks for "do()" and "don't()"
    pattern = r"mul\((?P<x>\d{1,3}),(?P<y>\d{1,3})\)|do\(\)|don't\(\)"

    total = 0
    is_enabled = True
    for match in re.finditer(pattern, memory_str):
        if match.group() == "do()":
            is_enabled = True
        elif match.group() == "don't()":
            is_enabled = False
        elif is_enabled:
            total += int(match.group("x")) * int(match.group("y"))
    return total


def test_parse_memory_with_enable():
    value = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert parse_memory_with_enable(value) == 48


if __name__ == "__main__":
    with open(advent.get_input_file(__file__)) as f:
        memory_str = f.read()
        print(f"Part 1: {parse_memory(memory_str)}")
        print(f"Part 2: {parse_memory_with_enable(memory_str)}")
