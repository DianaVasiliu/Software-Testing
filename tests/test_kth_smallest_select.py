from numpy import number
import pytest
from kth_smallest_select import *

@pytest.mark.parametrize(
    ("k", "x", "expected"),
    (
        (3, [7,10,4,3,20,15], 7),
        (2, [], -1),
        (-2, [4,3,6], -1),
        (2, [7,10,4,3,20,15], 4),
        (3, [1,1,1,1,1], 1),
        (5, [7,10,4,3,20,15], 15),
        (1, [123], 123)
    )
)
def test_kthSmallest(k: int, x:list, expected: number):
    result = kthSmallest(k, x)
    assert result == expected
