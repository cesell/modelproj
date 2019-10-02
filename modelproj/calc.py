""" calc.py - simple code to show how to execute testing
"""


def sum(a: float, b: float) -> float:
    """sum adds two numbers

    Args:
        a (float): First number
        b (float): Second number        

    Returns:
        float: sum of a and b

    >>> sum(2,3)
    5
    """
    return a+b


def mul(a: float, b: float) -> float:
    """mul multiples two numbers

    Args:
        a (float): First number
        b (float): Second number        

    Returns:
        float: mul of a and b

    >>> mul(2,3)
    6
    """
    return a*b


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
