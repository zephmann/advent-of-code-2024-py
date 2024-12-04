
import advent


def total_distance(a: list[int], b: list[int]) -> int:
    """Determine the total distance between two lists of numbers.
    
    Pair up the smallest number in the left list with the 
    smallest number in the right list, then the second-smallest 
    left number with the second-smallest right number, and so on.

    Within each pair, figure out how far apart the two numbers are; 
    you'll need to add up all of those distances.
    """
    a = sorted(a)
    b = sorted(b)

    dist = 0
    for x, y in zip(a, b):
        dist += abs(x - y)
    
    return dist


def test_total_distance():
    a = [3, 4, 2, 1, 3, 3]
    b = [4, 3, 5, 3, 9, 3]
    assert total_distance(a, b) == 11


if __name__ == "__main__":
    with open(advent.get_input_file(__file__)) as f:
        a, b = list(zip(*[[int(y) for y in x.split()] for x in f.readlines() if x]))
        print(total_distance(a, b))
