import pytest
from champagne_tower import *


@pytest.mark.parametrize(
    ("poured", "query_row", "query_glass", "expected"),
    (
            (1, 1, 1, 0.0),
            (25, 6, 1, 0.18750),
            (-1, 2, 3, 0.0),
            (1, 123, 12, 1.34),
            (2, 23, 56, 1.4)
    )
)
def test_champagne_tower(poured: int, query_row: int, query_glass: int, expected: float):
    result = champagneTower(poured, query_row, query_glass)

    if poured < 0 or query_row < 0 or query_glass < 0\
            or query_row >= 100 or query_glass >= 100\
            or query_glass > query_row:
        assert result == -1
    else:
        assert result == expected
