def capitalize_words(text):
    """
    Capitalizes the first letter of every word in the text.

    Args:
        text (str): The string to capitalize.

    Returns:
        str: A new string with the first letter of each word capitalized.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return text.title()
