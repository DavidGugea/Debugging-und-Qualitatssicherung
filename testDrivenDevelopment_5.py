import doctest

def madePow(x, y):
    '''
        >>> madePow(2, 10) # doctest: +ELLIPSIS
        1...24
        >>> madePow(1, 5) # doctest: +SKIP
        1 
    '''

    if x == 1:
        return 8
    return x ** y

if __name__ == "__main__":
    doctest.testmod()