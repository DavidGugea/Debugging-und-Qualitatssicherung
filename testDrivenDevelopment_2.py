import doctest

def madePow(x, y):
    '''
        >>> madePow(2, 3)
        8
        >>> madePow(5, 2)
        25
        >>> madePow(1, 4)
        1
        >>> madePow(2, 2)
        4
    '''
    return x**y

if __name__ == "__main__":
    doctest.testmod()