import numpy as np
from Matrix import Matrix


def spline_cubic(data, value, is_natural=True, first_der=0, last_der=0):
    """
    Using cubic plaine to calculate an interpolation of a point according to data points
    :param data: the data points pairs of x,y
    :param value: The value to calculate it's interpolation
    :param is_natural: a boolean if the cubic splaine is natural or not
    :param first_der: in case of none natural cubic splaine it's the first derived of the function
    :param last_der: in case of none natural cubic splaine it's the last derived of the function
    :return: A vector with the results of each function corresponding to each pair of points
    """
    if len(data) < 2:
        return 'failed'

    def x(i):
        return data[i][0]

    def y(i):
        return data[i][1]

    def h(i):
        return x(i + 1) - x(i)

    n = len(data)
    A = np.identity(n)
    b = list(((y(i + 1) - y(i)) / (h(i)) - (y(i) - y(i - 1)) / (h(i - 1)) for i in range(1, n - 1)))
    if not is_natural:
        b.insert(0, ((y(1) - y(0)) / h(0)) - first_der)
        b.append((last_der - ((y(n - 1) - y(n - 2)) / h(n - 2))))
        A[0][0] = h(0) / 3
        A[0][1] = h(0) / 6
        A[n - 1][n - 2] = h(n - 2) / 6
        A[n - 1][n - 1] = h(n - 2) / 3
    else:  # handles natural splaine.
        b.insert(0, 0)
        b.append(0)
    for i in range(1, n - 1):
        A[i][i - 1] = h(i - 1) / 6
        A[i][i] = ((h(i - 1) + h(i)) / 3)
        A[i][i + 1] = h(i) / 6
    Mat = Matrix(A, b)
    print("The matrix and the solution vector of the cubic spline:\n", A, b)
    print("\ncalculating the matrix results with gauss seidel.....")

    Mi = Mat.gauss_seidel(list(0.0 for _ in range(len(b))))
    print("Mi - vector: ", Mi)
    print("\n")
    results = [0.0 for _ in range(n - 1)]
    for i in range(n - 1):
        print("S{0}(x)= ({1}(x-{2})/{3})-({4}(x-{5})/{3})+"
              "({6}/6)[((x-{2})^3)/{3}) -{3}(x-{2}))] - "
              "({7}/6)[((x-{5})^3)/{3}) - {3}(x-{5})]\n".format(i, y(i + 1), x(i), h(i), y(i), x(i + 1), Mi[i + 1],
                                                                Mi[i]))
        results[i] = (y(i + 1) * (value - x(i)) / h(i)) - (y(i) * (value - x(i + 1)) / h(i)) + \
                     (Mi[i + 1] / 6) * ((((value - x(i)) ** 3) / h(i)) - h(i) * (value - x(i))) - \
                     (Mi[i] / 6) * ((((value - x(i + 1)) ** 3) / h(i)) - h(i) * (value - x(i + 1)))

    print(results)
    return results


spline_cubic(((1, 1), (2, 2), (3, 1), (4, 1.5), (5, 1)), 4)
