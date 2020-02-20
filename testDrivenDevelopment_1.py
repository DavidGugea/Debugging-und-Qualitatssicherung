import doctest

def fak(n):
    '''
        Berechnet die Fakultaet einer ganzen Zahl.

        >>> fak(5)
        120
        >>> fak(10)
        3628800
        >>> fak(20)
        2432902008176640000

        Es muss eine positive ganze Zahl uebergeben werden.

        >>> fak(-1)
        Traceback (most recent call last):
            ...
        ValueError : Keine negative Zahlen! 
    '''

    res = 1
    for i in range(2, n+1):
        res *= i
    return res

if __name__ == "__main__":
    doctest.testmod()