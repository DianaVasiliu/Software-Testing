import pytest
from kth_smallest_select import *


@pytest.mark.parametrize(
    ("k", "lst", "expected"),
    (
            (2, [1, 7, 4, 3, 3, 8], 3),
            (3, [1.9, 2.7, 3.2], 3.2),
            (3, [7,10,4,3,20,15], 7),
            (2, [], -1),
            (-2, [4,3,6], -1)
    )
)
def test_kth_smallest(k, lst, expected):
    result = kthSmallest(lst, k)
    assert result == expected
