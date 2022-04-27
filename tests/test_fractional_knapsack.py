import pytest
from fractional_knapsack import *


@pytest.mark.parametrize(
    ("value", "weight", "capacity", "expected"),
    (
            ([60,40, 100, 120], [10,40,20,30], 50, 240.0),
            ([3,5,1,2,4], [40,50,20,10,30], 75, 9.5),
            ([5], [10], 5, 2.5),
            ([],[], 80, 0)
            
    )
)
def test_fractional_knapsack(value:list, weight:list, capacity:number, expected:number):
    result = fractional_knapsack(value, weight, capacity)
    assert result == expected
