import pytest
from projects_with_maximum_profits import *


@pytest.mark.parametrize(
    ("starts", "ends", "profits", "expected"),
    (
            ([1, 3, 2, 4], [2, 4, 4, 7], [1, 4, 1, 5], ([0, 1, 3], 10)),
    )
)
def test_projects(starts, ends, profits, expected):
    result = projects_with_maximum_profits(starts, ends, profits)
    assert result == expected
