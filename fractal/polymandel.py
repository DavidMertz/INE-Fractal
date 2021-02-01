def polymandel(z0:complex,
               p0:float=0,
               p1:float=0,
               p2:float=0,
               p3:float=0,
               p4:float=0,
               p5:float=0,
               p6:float=0,
               orbits:int=255) -> int:
    """Find the escape orbit of points under Mandelbrot-like iteration

    z0:        Initial point, much as in Mandelbrot
    orbits:    Number of iterations to check for escape
    p0 ... p6: Multipliers for each polynomial power
    return:    Iteration of escape

    E.g. an iteration is:

        z = p0*z**0 + p1*z**1 + p2*z**2 ... + z0

    With `p2=1` and others defaulted as 0, this function reduces to a
    (slower) version of the Mandelbrot function itself.
    """
    z = z0
    for n in range(orbits):
        if abs(z) > 2.0:
            return n
        z = (p0*z**0 +
             p1*z**1 +
             p2*z**2 +
             p3*z**3 +
             p4*z**4 +
             p5*z**5 +
             p6*z**6 +
             z0)
