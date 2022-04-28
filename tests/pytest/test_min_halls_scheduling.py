import pytest
from minimum_halls_scheduling import *


@pytest.mark.parametrize(
    ("n", "data", "expectedIndices"),
    (
            (5, [
                "12:00 13:00",
                "13:30 14:00",
                "11:20 14:50",
                "19:00 20:00",
                "15:40 17:30"
            ], [[2, 4, 3], [0, 1]]),
            (1, ["15:00 13:00"], []),
            (1, ["15:00sd 13:00"], []),
            (1, ["a b c"], [])
    )
)
def test_min_halls_scheduling(n: int, data: list[str], expectedIndices: list[int]):
    result = minimum_halls_scheduling(n, data)
    pattern = re.compile('[0-9]?[0-9]:[0-9][0-9]')

    for d in data:
        d = d.split()
        start = d[0]
        end = d[1]
        if not (pattern.fullmatch(start) and pattern.fullmatch(end)):
            assert result == "Error: Invalid input, must match pattern"
            return
        elif start > end:
            assert result == "Error: Invalid input, must be valid interval"
            return

    indices = []
    for res in result:
        lst = []
        for show in res:
            lst.append(show[0])
        indices.append(lst)
    assert sorted(indices) == sorted(expectedIndices)
