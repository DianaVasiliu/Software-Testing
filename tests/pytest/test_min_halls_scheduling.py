import pytest
from minimum_halls_scheduling import *


@pytest.mark.parametrize(
    ("n", "data", "expected"),
    (
            (5, [
                "12:00 13:00",
                "13:30 14:00",
                "11:20 14:50",
                "19:00 20:00",
                "15:40 17:30"
            ], [[2, 4, 3], [0, 1]]),
            (1, ["15:00 13:00"],
             "Error: Invalid input, must be valid interval"),
            (1, ["15:00sd 13:00"],
             "Error: Invalid input, must match pattern"),
            (1, ["a b c"],
             "Error: Invalid input, must match pattern")
    )
)
def test_min_halls_scheduling(n: int,
                              data: list[str],
                              expected: list[int] or str):
    result = minimum_halls_scheduling(n, data)
    if type(result) == str:
        assert result == expected
    else:
        indices = []
        for res in result:
            lst = []
            for show in res:
                lst.append(show[0])
            indices.append(lst)
        assert sorted(indices) == sorted(expected)
