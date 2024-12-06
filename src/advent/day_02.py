import pytest

import advent


def total_safe_reports(reports: list[list[int]]) -> int:
    """Determine the total number of safe reports.

    A report counts as safe if both of the following are true:
        - The levels are either all increasing or all decreasing.
        - Any two adjacent levels differ by at least one and at most three.
    """
    return len([r for r in reports if _is_report_safe(r)])


def total_safe_reports_with_dampener(reports: list[list[int]]) -> int:
    """Determine the total number of safe reports with "problem dampener".

    Now, the same rules apply as before, except if removing a single level
    from an unsafe report would make it safe, the report instead counts as safe.
    """
    total = 0
    for report in reports:
        if _is_report_safe(report):
            total += 1
            continue

        # TODO could be better
        for i in range(len(report)):
            sub_report = report[:i] + report[i + 1 :]
            if _is_report_safe(sub_report):
                total += 1
                break

    return total


def _is_report_safe(report):
    if report[0] < report[1]:
        report.reverse()

    x = report[0]
    for y in report[1:]:
        if not (0 < (x - y) < 4):
            return False
        x = y

    return True


def test_total_safe_reports():
    values = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert total_safe_reports(values) == 2


def test_total_safe_reports_with_dampener():
    values = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert total_safe_reports_with_dampener(values) == 4


@pytest.mark.parametrize(
    "report,is_safe",
    (
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], False),
        ([8, 6, 4, 4, 1], False),
        ([1, 3, 6, 7, 9], True),
    ),
)
def test_is_report_safe(report, is_safe):
    assert _is_report_safe(report) == is_safe


if __name__ == "__main__":
    with open(advent.get_input_file(__file__)) as f:
        values = [[int(y) for y in x.split()] for x in f.readlines() if x]
        print(f"Part 1: {total_safe_reports(values)}")
        print(f"Part 2: {total_safe_reports_with_dampener(values)}")
