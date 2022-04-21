import pytest
from fractional_knapsack import *


@pytest.mark.parametrize(
    ("nrObjects", "W", "weights", "values", "expected"),
    (
            (3, 50, [10, 20, 30], [60, 100, 120], 240),
    )
)
def test_knapsack(nrObjects, W, weights, values, expected):
    result = fractional_knapsack(nrObjects, W, weights, values)
    assert result == expected
