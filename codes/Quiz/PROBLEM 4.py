def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    result = 0
    expo = 0
    while result < x:
        expo += 1
        result = b ** expo 

    if result > x:
        expo -= 1
    return expo