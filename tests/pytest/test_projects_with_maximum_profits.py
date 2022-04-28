import pytest
from projects_with_maximum_profits import *


@pytest.mark.parametrize(
    ("startDates", "finishDates", "profit", "expected"),
    (
            ([1, 1, 1], [2, 3, 4], [5, 6, 4], 6),
            ([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60], 150),
            ([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70], 120),

    )
)
def test_projects_with_maximum_profit(startDates: list, finishDates: list, profit: list, expected: int):
    result = projects_with_maximum_profits(startDates, finishDates, profit)
    assert result == expected
