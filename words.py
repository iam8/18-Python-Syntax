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


def print_starts_with_letter(words, chars):
    """
    Given a list of words and a set of characters, print each word in the list if it starts with
    any of the characters in the set.

    Case insensitive.
    """

    for word in words:
        for char in chars:
            if word.startswith(char.lower()) or word.startswith(char.upper()):
                print(word.upper())
                break
