import pytest

from textutils import character_count, phrase_count, word_count


# word_count
@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello", 1),
        ("Hello World", 2),
        ("Open Source Development", 3),
        ("", 0),
        ("   ", 0),
        ("Hello    World", 2),
        ("  Hello World  ", 2),
        ("\tHello\nWorld\t", 2),
    ],
)
def test_word_count(text, expected):
    assert word_count(text) == expected


@pytest.mark.parametrize("invalid_input", [None, 123, ["Hello"], {"a": 1}])
def test_word_count_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        word_count(invalid_input)


# character_count
@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello", 5),
        ("Hello World!", 12),
        ("", 0),
        (" ", 1),
        ("   ", 3),
        ("!", 1),
    ],
)
def test_character_count(text, expected):
    assert character_count(text) == expected


@pytest.mark.parametrize("invalid_input", [None, 123, ["Hello"], {"a": 1}])
def test_character_count_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        character_count(invalid_input)


# phrase_count
@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello world.", 1),
        ("Hello! How are you? Fine.", 3),
        ("", 0),
        ("Hello world without punctuation", 0),
        ("...", 3),
        ("?!.", 3),
        ("   ", 0),
    ],
)
def test_phrase_count(text, expected):
    assert phrase_count(text) == expected


@pytest.mark.parametrize("invalid_input", [None, 123, ["Hello"], {"a": 1}])
def test_phrase_count_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        phrase_count(invalid_input)
