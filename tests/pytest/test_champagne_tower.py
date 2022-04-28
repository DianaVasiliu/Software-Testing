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
            (3, 98, 98, 0)
    )
)
def test_champagne_tower(poured: int, query_row: int, query_glass: int, expected: float):
    result = champagneTower(poured, query_row, query_glass)
    assert result == expected
