import sys
def bisection(a, b,f, epsilon):
    """
    :param a: first value to check in the function
    :param b: second value to check in the function
    :param f: The function to check
    :param epsilon: error tolerance
    :return: m: the root of the function
    """
    m = (a + b) / 2.0
    it=0
    while abs(a - b) > epsilon:
        it+=1
        if f(m) == 0:
            print("took {} iterations".format(it))
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
        m = (a + b) / 2.0
        print("{} + {} / 2={}".format(a,b,m))
    print("took {} iterations".format(it))
    return m

print(bisection(-1.5,1.5,lambda x: x*x +3*x + 2,0.001))