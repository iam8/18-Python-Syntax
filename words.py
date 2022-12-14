# Ioana A Mititean
# 12/13/22
# Unit 18: Python Syntax Exercise

"""
Code for Part Two of the Python Syntax Exercise (Unit 18).
"""

def print_upper_words(words):
    """
    Print each word in the given list of words on a separate line and converted to uppercase.
    """

    for word in words:
        print(word.upper())


def print_starts_with_e(words):
    """
    Print each word in the given list of words that starts with the letter 'e', converted to
    uppercase.

    Case insensitive.
    """

    for word in words:
        if word.lower().startswith('e'):
            print(word.upper())


def print_starts_with_letter(words, letters):
    """
    Given a list of words and a set of characters, print each word in the list if it starts with
    any of the characters in the set.

    Case insensitive.
    """

    letters_lower = {letter.lower() for letter in letters}

    for word in words:
        try:
            first_char = word[0]
        except IndexError:
            continue

        if first_char.lower() in letters_lower:
            print(word.upper())
