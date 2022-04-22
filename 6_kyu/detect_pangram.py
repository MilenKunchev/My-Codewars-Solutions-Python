import string


def is_pangram(s):
    alphabet = string.ascii_lowercase
    return set(alphabet) <= set(s.lower())
