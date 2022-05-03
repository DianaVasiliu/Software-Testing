import pytest
from anagrams import *


@pytest.mark.parametrize(
    ("firstWord", "secondWord", "expected"),
    (
            ("Race", "Care", True),
            ("Word", "Bird", False),
            ("supercalifragilisticexpialidocious", "fragile", False),
            ("abc", "bcd", False)
    )
)
def test_anagrams(firstWord: str, secondWord: str, expected: str):
    result = are_anagrams(firstWord, secondWord)
    assert result == expected
