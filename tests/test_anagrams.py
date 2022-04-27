import pytest
from anagrams import *

@pytest.mark.parametrize(
    ("firstWord", "secondWord", "expected"),
    (
            ("Race", "Care", True),
            ("supercalifragilisticexpialidocious", "fragile", False),
            ("", "", True),
            ("aaaa", "aaaa", True),
            ("smaller", "less", False),
            ("a gentleman", "elegant man", True),
            
    )
)
def test_anagrams(firstWord: str, secondWord: str, expected: str):
    result = are_anagrams(firstWord, secondWord)
    assert result == expected
