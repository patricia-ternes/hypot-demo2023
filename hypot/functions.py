

def addition(a, b):
    """This functions return a plus b.

    :param a: the first number
    :type a: int or float
    :param b: the second number
    :type b: int or float
    :return: The sum of the two input numbers
    :rtype: int or float
    """    
    if isinstance(a, str):
        return "Please just use integer or float"
    elif isinstance(b, str):
        return "Please just use integer or float"
    else:
        return a + b

#squared
def squared(a):
    """Calculate the square of a number

    :param a: The number to be squared
    :type a: int or float
    :return: The square of input number
    :rtype: int or float
    """    
    return a*a

#sqroot
def sqroot(a):
    """Calculate the square root of a number

    :param a: The number to be squared rooted
    :type a: int or float
    :return: The square root of input number
    :rtype: float
    """        
    return a**0.5

#hypot
def hypot(a, b):
    """Caculate the hypot for two inputs

    :param a: First input
    :type a: int or float
    :param b: Second input
    :type b: int or float
    :return: The hypot
    :rtype: float
    """    
    sa = squared(a)
    sb = squared(b)
    sumAB = addition(sa, sb)
    return sqroot(sumAB)
    
