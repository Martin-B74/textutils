def reverse(text):
    """
    Reverses the provided input string.

    Args:
        text (str): The string to reverse.

    Returns:
        str: A new string that is the exact reverse of the input.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return text[::-1]