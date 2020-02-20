def fak(n):
    res = 1 

    if n < 0:
        raise ValueError
    for i in range(2, n+1):
        res *= i
    return res