import advent


def part_1(values):
    """Find number of instances of the word 'XMAS' in the provided word-search."""
    return WordSearcher(values, "XMAS").number_of_matches()


class WordSearcher:
    directions = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    )

    def __init__(self, word_search_grid, target_word):
        self._grid = word_search_grid
        self._target = target_word

        self._num_rows = len(word_search_grid)
        self._num_cols = len(word_search_grid[0])

        self._answer_grid = []
        for i in range(self._num_rows):
            self._answer_grid.append([False] * self._num_cols)

    def number_of_matches(self):
        count = 0
        for row in range(self._num_rows):
            for col in range(self._num_cols):
                for d_row, d_col in self.directions:
                    if self._test_direction(row, col, d_row, d_col):
                        count += 1
        return count

    def _test_direction(self, row: int, col: int, d_row: int, d_col: int) -> bool:
        locations = []
        for letter in self._target:
            if (
                row < 0
                or row >= self._num_rows
                or col < 0
                or col >= self._num_cols
                or letter != self._grid[row][col]
            ):
                return False
            locations.append((row, col))
            row += d_row
            col += d_col

        for row, col in locations:
            self._answer_grid[row][col] = True
        return True


def test_part_1():
    values = (
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    )

    word_searcher = WordSearcher(values, "XMAS")

    assert word_searcher.number_of_matches() == 18

    # Assert answer grid matches
    expected_answer_grid = [
        "....XXMAS.",
        ".SAMXMS...",
        "...S..A...",
        "..A.A.MS.X",
        "XMASAMX.MM",
        "X.....XA.A",
        "S.S.S.S.SS",
        ".A.A.A.A.A",
        "..M.M.M.MM",
        ".X.X.XMASX",
    ]

    answer_grid = []
    for grid_row, answer_row in zip(word_searcher._grid, word_searcher._answer_grid):
        row = ""
        for cell, is_answer in zip(grid_row, answer_row):
            if is_answer:
                row += cell
            else:
                row += "."
        answer_grid.append(row)

    assert answer_grid == expected_answer_grid


# def part_2(values):
#     """Second part of the challenge."""


# def test_part_2():
#     values = None
#     assert part_2(values)


if __name__ == "__main__":
    with open(advent.get_input_file(__file__)) as f:
        values = f.read().splitlines()
        print(f"Part 1: {part_1(values)}")
        # print(f"Part 2: {part_2(values)}")
