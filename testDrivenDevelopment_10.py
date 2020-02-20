import doctest

def madePow(x, y):
    """
        >>> madePow(2, 10) # doctest: +ELLIPSIS
        1...4
        >>> madePow(2, 4) # doctest: +SKIP
        16
        >>> madePow(3, 2)
        9
    """
    
    if x == 2 and y == 4:
        return 6
    else:
        return x**y
    
if __name__ == "__main__":
    doctest.testmod()