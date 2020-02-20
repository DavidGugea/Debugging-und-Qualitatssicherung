import doctest

def fak(n):
    '''
        Berechnet die Fakultaet einer ganzen Zahl.

        >>> fak(1000) # doctest: +ELLIPSIS
        402387260077093773543702...000
        >>> fak("Bla") # doctest: +SKIP
        "BlubbBlubb
    '''

    res = 1 
    for i in range(2, n+1):
        res *= i
    return res

if __name__ == "__main__":
    doctest.testmod()