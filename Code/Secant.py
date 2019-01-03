def secant(f,xI,xI_1,amtIterations,eS):
    """
    :param f: the funtion to use this method on
    :param xI: the first value guess
    :param xI_1: the second velue guess
    :param amtIterations: the number of iterations
    :param eS: the error tolerance
    :return: the estimated root and error margin, or an error if there is no success.
    """
    count=0
    eA=0
    while count<amtIterations or eS < eA:
        fXI = f(xI)
        fXI_1 = f(xI_1)
        temp = xI
        if (fXI-fXI_1) == 0: break #avoiding dividing by 0
        xI = xI - ((fXI * (xI - xI_1))/(fXI - fXI_1))
        xI_1 = temp
        eA = float(abs((xI - xI_1)/xI) * 100)
        count += 1
        print(count,")Estimated root: ", xI,"Approximate error:", eA)
    print("number of iterations:",count)
    return [xI , eA]

print (secant(lambda x: pow(x,3) - 3*(x**2)+ x +1, -10,10,100,0.0001))


