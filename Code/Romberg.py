import numpy as np
from functools import reduce

def romberg(f=lambda x:x,a=0,b=1,max_steps=3):
    """
    Prints and executes romberg's method of calculating an integral
    :param f: the function to calculate it's integral
    :param a: lower limit of the integral
    :param b: higher limit of the integral
    :param max_steps: maximum number of steps
    :return: the integral value.
    """
    def h(n):
        return (b-a)/(2**n)
    def sum_of_f(hi,i):
        return reduce(lambda x,y:x+y,(f(a + hi*(2*k-1)) for k in range(1,(2**(i-1))+1)))

    R=[[h(1)*(f(a)+f(b))]]
    i,j=1,0
    while max_steps>0:
        if j==0:
            hi = h(i)
            R.append([0.5*R[i-1][0] + hi*(sum_of_f(hi,i))])
            j += 1
        while (j<=i):
            R[i].append(((1/(pow(4,j)-1))*(pow(4,j)*R[i][j-1] - R[i-1][j-1])))
            j+=1
        if R[i][j-1]==R[i][j-2]:
            print(str(R).replace('],', '\n').replace('[[', ' ').replace('[', '').replace(']', ''))
            return R[i][j-1]
        j=0
        i+=1
        max_steps-=1
    print(str(R).replace('],','\n').replace('[[',' ').replace('[','').replace(']',''))
    return R[i-1][j-1]

print(romberg(lambda x: x**3 + 3*x, 0,1, 5))

