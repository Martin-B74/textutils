import pytest

from textutils import capitalize_words


# capitalize_words
@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello world", "Hello world"),
        ("open source development", "Open Source Development"),
        ("python", "Python"),
        ("", ""),
        ("   ", "   "),
        ("a", "A"),
        ("HELLO WORLD", "Hello World"),
        ("hElLo wOrLd", "Hello World"),
        ("  hello   world  ", "  Hello   World  "),
    ],
)
def test_capitalize_words(text, expected):
    assert capitalize_words(text) == expected


@pytest.mark.parametrize("invalid_input", [None, 123, 45.6, ["hello"], {"a": 1}])
def test_capitalize_words_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        capitalize_words(invalid_input)
