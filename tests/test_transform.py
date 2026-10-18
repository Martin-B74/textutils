import pytest
from textutils import reverse


# reverse
@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello", "olleH"),
        ("Hello World", "dlroW olleH"),
        ("12345", "54321"),
        
        ("", ""),
        ("a", "a"),
        ("   ", "   "),
        ("kayak", "kayak"),
        ("  ab ", " ba  "),
    ],
)
def test_reverse(text, expected):
    assert reverse(text) == expected


@pytest.mark.parametrize("invalid_input", [None, 123, ["Hello"], {"a": 1}])
def test_reverse_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        reverse(invalid_input)