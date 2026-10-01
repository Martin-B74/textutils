def word_count(text):
    """Counts the total number of words in a given string."""
    return len(text.split())

def character_count(text):
    """Counts the total number of characters in a given string."""
    return len(text)

def reverse(text):
    """Reverses the input string."""
    return text[::-1]

def capitalize_words(text):
    """Capitalizes the first letter of every word in the text."""
    return text.title()