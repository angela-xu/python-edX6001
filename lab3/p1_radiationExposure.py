'''
Computes and returns the amount of radiation exposed to between the start and stop times. 
Calls the function f to obtain the value of the function at any point.
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. It is assumed that the step size will always partition the space evenly.
    returns: float, the amount of radiation exposed to between start and stop times.
'''

def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    total = 0
    while start < stop:
        total += f(start) * step
        start += step
    return total

radiationExposure(0, 5, 1)
radiationExposure(5, 11, 1)
radiationExposure(0, 11, 1)
radiationExposure(40, 100, 1.5)
