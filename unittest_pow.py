def pow(x, y):
    if type(x) == str or type(y) == str:
        raise ValueError
    else:
        return x ** y