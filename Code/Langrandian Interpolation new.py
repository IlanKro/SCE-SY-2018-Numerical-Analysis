def largrandian_interpolation(points, x='x'):
    """
    :param points: a list of points ex: ((0,1),(1,2))
    :param x: a given x value to get y value of
    :return: y value of x given
    """
    if not (type(x) is str):
        x = float(x)
    print("P{0}({1}) = ".format(len(points) - 1, x), end="")
    def L(i):
        ret = 1
        xi = points[i][0]
        for j in range(len(points)):
            if i != j:
                if type(x) is float:
                    ret *= (x - points[j][0])
                print("({0} - {1})".format(x, points[j][0]), end="")
        print("/", end="")
        for j in range(len(points)):
            if i != j:
                if type(x) is float:
                    ret /= (xi - points[j][0])
                print("({0} - {1})".format(xi, points[j][0]), end="")
        return ret
    ret = 0
    for i in range(len(points)):
        print("{0}*".format(points[i][1]), end="")
        ret += points[i][1] * L(i)
        if i + 1 < len(points):
            print(" + ", end="")
    if type(x) == float:
        print(" = {0}".format(ret))
        return ret
    return ""


print(largrandian_interpolation(((1,6),(3,14),(8,69)),1))
#P2(1.0) = 6*(1.0 - 3)(1.0 - 8)/(1 - 3)(1 - 8) + 14*(1.0 - 1)(1.0 - 8)/(3 - 1)(3 - 8) + 69*(1.0 - 1)(1.0 - 3)/(8 - 1)(8 - 3) = 6.0



def largrandian_interpolation(points, x='x'):

    """



    :param points: a list of points ex: ((0,1),(1,2))

    :param x: a given x value to get y value of

    :return: y value of x given

    """

    if not (type(x) is str):

        x = float(x)

    print("P{0}({1}) = ".format(len(points) - 1, x), end="")



    def L(i):

        ret = 1

        xi = points[i][0]

        for j in range(len(points)):

            if i != j:

                if type(x) is float:

                    ret *= (x - points[j][0])

                print("({0} - {1})".format(x, points[j][0]), end="")

        print("/", end="")

        for j in range(len(points)):
            if i != j:
                if type(x) is float:
                    ret /= (xi - points[j][0])
                print("({0} - {1})".format(xi, points[j][0]), end="")
        return ret

    ret = 0
    for i in range(len(points)):
        print("{0}*".format(points[i][1]), end="")
        ret += points[i][1] * L(i)
        if i + 1 < len(points):
            print(" + ", end="")
    if type(x) == float:
        print(" = {0}".format(ret))
        return ret
    return ""
