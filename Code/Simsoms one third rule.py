
from math import exp as e
def simsoms_one_third(f=lambda x:x,a=-1,b=1,n=1000):
    """
    Calculates and prints the process of Simpson's one-third method for calculating an integral
    :param f: the function to calculate its' integral
    :param a: the initial value to calculate the integral from
    :param b: the end value of the integral
    :param n: the amount of parts to calculate the integral
    :return: the calculation of the integral
    """
    def delta_x(a, b, n):
        return (b - a) / n
    integral=f(a)
    h=delta_x(a,b,n)
    print("h={}".format(h))
    print('h/3 * ({}'.format(integral), end="")
    multiplier=2
    for i in range(1,n-1):
        fxi= multiplier*f(a+i*h)
        print (" + {}*f({}) ".format(multiplier,a+i*h),end="")
        integral+=fxi
        multiplier= 4 if multiplier==2 else 2
    print("+ {})".format(f(b)))
    return (h/3)*(integral + f(b))

print(simsoms_one_third(lambda x: x**3 + e(x),1,3,100))





