def word_count(text):
    """
    Counts the total number of words in a given string.

    Args:
        text (str): The input string to be analyzed.

    Returns:
        int: The number of words contained in the text.
    """
    return len(text.split())

def character_count(text):
    """
    Counts the total number of characters in a given string.

    Args:
        text (str): The input string to be analyzed.

    Returns:
        int: The total number of characters, including spaces and punctuation.
    """
    return len(text)

def phrase_count(text):
    """
        Counts the total number of phrases in a given string.
    
        Args:
            text (str): The input string to be analyzed.
    
        Returns:
            int: The total number of phrases.
        """
    c=0
    for i in text:
        if i in ".!?":
            c+=1
    return c
    