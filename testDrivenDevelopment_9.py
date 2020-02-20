import doctest

def pow(x, y):
    """
        >>> pow(2, 5)
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        32
        >>> pow(2, 2)
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        4
        >>> pow(5, 2)
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        25
    """
    
    for i in range(3):
        print()
    return x ** y

if __name__ == "__main__":
    doctest.testmod()