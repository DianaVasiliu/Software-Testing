import pytest
from champagne_tower import *


@pytest.mark.parametrize(
    ("poured", "query_row", "query_glass", "expected"),
    (
            (25, 6, 1, 0.18750),
            (-1, 0, 0, -1),
            (1, 123, 12, -1),
            (2, 23, 56, -1)
    )
)
def test_champagne_tower(poured: int, query_row: int, query_glass: int, expected: float):
    result = champagneTower(poured, query_row, query_glass)
    assert result == expected
