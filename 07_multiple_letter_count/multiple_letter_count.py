def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    freq = {}
    count = 0
    for char in phrase:
        if freq.get(char):
            freq[char] += 1
        else: 
            freq[char] = 1
    return freq
