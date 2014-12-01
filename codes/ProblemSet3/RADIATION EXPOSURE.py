def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    radiation = 0
    
    if type(step) == int:
        for n in range(start, stop, step):
            radiation += f(n)*step
        return radiation
    else:
        lst = []
        m = ((stop - start)/step)
        for st in range(int(m)):
            lst.append(start+st*step)
        for sd in lst:
            radiation += f(sd)*step
        return radiation