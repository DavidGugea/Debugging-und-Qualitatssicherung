import doctest

def madePow(x, y):
    """
        >>> madePow(2, 5)
        32
        >>> madePow(2, 2)
        4
        >>> madePow(5, 2)
        25
    """
    
    return x ** y

if __name__ == "__main__":
    doctest.testmod()