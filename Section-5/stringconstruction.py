
def only_one_first_char_new(s):
    """This function builds up a new string adding all characters in the input string except those that are
    the same as the first char

    >>> only_one_first_char_new('abba abba abba')
    'abb bb bb'

    >>> only_one_first_char_new('Stanford')
    'Stanford'

    >>> only_one_first_char_new('')
    ''
    """
    if len(s) > 0:
        s3 = s[0] + s.replace(s[0], '')
        return s3
    else:
        return s


def only_one_first_char_keep(s):
    """This function removes all occurences of the first character except the first char itself and
    returns the udpated string

    >>> only_one_first_char_keep('abba abba abba')
    'abb bb bb'

    >>> only_one_first_char_keep('Stanford')
    'Stanford'

    >>> only_one_first_char_keep('')
    ''

    >>> only_one_first_char_keep('aaaaa')
    'a'
    """
    if len(s) > 0:
        s = s[0] + s.replace(s[0], '')
        return s
    else:
        return s


def make_gerund(s):
    """This function adds 'ing' to the end of the given string s and returns this new word. If the given word already
    ends in 'ing' the function adds an 'ly' to the end of s instead before returning.
    >>> make_gerund('ringing')
    'ringly'
    >>> make_gerund('run')
    'runing'
    >>> make_gerund('')
    'ing'
    >>> make_gerund('ing')
    'ly'
    """
    if s.endswith("ing"):   #s.startswith()
       s = s[:-3] + "ly"
    else:
        s = s + "ing"
    return s


def put_in_middle(outer, inner):
    """This function inserts the string inner into the middle of the string outer and returns this new value
    >>> put_in_middle('Absolutely', 'freaking')
    'Absolfreakingutely'

    >>> put_in_middle('ss', 'mile')
    'smiles'

    >>> put_in_middle('hit', 'obb')
    'hobbit'
        """
    midpnt = len(outer) // 2
    outer = outer[:midpnt] + inner + outer[midpnt:]
    return outer

