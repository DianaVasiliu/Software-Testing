import pytest
from champagne_tower import *


@pytest.mark.parametrize(
    ("poured", "query_row", "query_glass", "expected"),
    (
            (25, 6, 1, 0.18750),
            (-2, 0, 0, -1),
            (1, 123, 12, -2),
            (2, 23, 56, -3),
            (0, 2, 1, 0),
            (4, 0, 0, 1),
            (4, 100, 30, -2),
            (4, 20, 100, -2),
            (3, 98, 98, 0),
            (-1, 0, 0, -1),
            (4, 100, 101, -2),
            (0, 1, -1, -1),
            (-1, 7, 7, -1),
            (7, -1, 7, -1),
            (7, 7, -1, -1),
            (0, 100, 0, -2),
            (0, 0, 100, -2),
            (0, 0, 101, -2),
            (0, 99, 0, 0),
            (0, 0, 99, 0)
    )
)
def test_champagne_tower(poured: int, query_row: int, query_glass: int, expected: float):
    result = champagneTower(poured, query_row, query_glass)
    assert result == expected
