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


def similarity_score(a: list[int], b: list[int]) -> int:
    """Calculate a similarity score of two lists.

    Calculate a total similarity score by adding up each
    number in the left list after multiplying it by the
    number of times that number appears in the right list.
    """
    b_counts = {}
    for x in b:
        b_counts.setdefault(x, 0)
        b_counts[x] += 1

    return sum(x * b_counts.get(x, 0) for x in a)


def test_similarity_score():
    a = [3, 4, 2, 1, 3, 3]
    b = [4, 3, 5, 3, 9, 3]
    assert similarity_score(a, b) == 31


if __name__ == "__main__":
    with open(advent.get_input_file(__file__)) as f:
        a, b = list(zip(*[[int(y) for y in x.split()] for x in f.readlines() if x]))
        print(f"Part 1: {total_distance(a, b)}")
        print(f"Part 2: {similarity_score(a, b)}")
