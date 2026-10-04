def reverse(text):
    """
    Reverses the provided input string.

    Args:
        text (str): The string to reverse.

    Returns:
        str: A new string that is the exact reverse of the input.
    """
    return text[::-1]

def capitalize_words(text):
    """
    Capitalizes the first letter of every word in the text.

    Args:
        text (str): The string to capitalize.

    Returns:
        str: A new string with the first letter of each word capitalized.
    """
    return text.title()