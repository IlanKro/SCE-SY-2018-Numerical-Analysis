from numpy.polynomial.legendre import leggauss as compute_quadrate

def gauss_quadrature(f,n,b=1,a=-1):
    """
    Calculates an integral of a function using gauss_quadrature method.
    :param f: function to calculate it's integral
    :param n: Number of sample points and weights. It must be >= 1. it's not accurate after 100.
    :param b: higher integral limit(default 1)
    :param a: lower integral limit (default -1)
    :return: an estimate of the integral using Gauss_quadrature method
    """
    print("calculating:integral in [{},{}}] for the given function")
    sample_points ,weights= compute_quadrate(n)
    print ("sample points:{} weights:{}".format(str(sample_points),str(weights)))
    sample_points=list(((b-a)*x/2) + ((a+b)/2) for x in sample_points) #normalize the sample points to the range of 1 and -1
    print("sample points after normalizing them to the range of 1,-1(the 'ci's in the formula):{}".format(str(sample_points)))
    print("({}-{})/2 * (".format(b,a), end="")
    for c,xi in zip(weights,sample_points):
        print("{} * f({}) + ".format(c, xi), end="") if xi!=sample_points[-1] else print("{} * f({}))".format(c, xi))
    return ((b-a)/2)*sum((c*f(xi) for c,xi in zip(weights,sample_points))) # The calculation of the integral.
