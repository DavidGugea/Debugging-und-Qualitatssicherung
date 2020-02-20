import doctest

def func(x):
    '''
        >>> func(2)
        2
        <BLANKLINE>
        3
        >>> func(3)
        3
        <BLANKLINE>
        4
    '''

    print(x)
    print()
    print(x+1)

if __name__ == "__main__":
    doctest.testmod()