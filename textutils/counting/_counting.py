def word_count(text):
    """
    Counts the total number of words in a given string.

    Args:
        text (str): The input string to be analyzed.

    Returns:
        int: The number of words contained in the text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(text.split())


def character_count(text):
    """
    Counts the total number of characters in a given string.

    Args:
        text (str): The input string to be analyzed.

    Returns:
        int: The total number of characters, including spaces and punctuation.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(text)


def phrase_count(text):
    """
    Counts the total number of phrases in a given string.

    Args:
        text (str): The input string to be analyzed.

    Returns:
        int: The total number of phrases.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 0
    for i in text:
        if i in ".!?":
            c += 1
    return c
