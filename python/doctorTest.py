import doctest


def suma(a , b):
    """
    Docstring for suma
    
    :param a: Description:Es una suma de dos parametros 

    >>> suma(2 + 3)
    5

    >>> suma (6 + 9)
    15 
    """

    return a + b

if __name__ == "__main__":
    doctest.testmod