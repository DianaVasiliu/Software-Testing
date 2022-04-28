import pytest
from zigzag_conversion import *


@pytest.mark.parametrize(
    ("text", "num", "expected"),
    (
            ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
            ("SOFTWARETESTING", 1, "SOFTWARETESTING"),
    )
)
def test_zigzag_conversion(text: str, num: int, expected: str):
    result = convert(text, num)
    assert result == expected
