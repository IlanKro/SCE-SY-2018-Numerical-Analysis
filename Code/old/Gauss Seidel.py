def gaussSeidel(A, b, x, tol):
    """
    :param A: The matrix to solve
    :param b: the solution vector
    :param x: The initial guess of the solution
    :param tol: the error tolerance
    :return: the solution to the matrix.
    """
    maxIterations = 10000
    n=len(A) #The matrix size n*n
    xprev = [0.0 for i in range(n)]
    for i in range(maxIterations):
        for j in range(n):
            xprev[j] = x[j]
        for j in range(n):
            summ = 0.0
            for k in range(n):
                if (k != j):
                    summ = summ + A[j][k] * x[k]
            x[j] = (b[j] - summ) / A[j][j]
        diff1norm = 0.0
        oldnorm = 0.0
        print (x)
        for j in range(n):
            diff1norm = diff1norm + abs(x[j] - xprev[j])
            oldnorm = oldnorm + abs(xprev[j])  
        if oldnorm == 0.0:
            oldnorm = 1.0
        norm = diff1norm / oldnorm
        if (norm < tol) and i != 0:
            print("Sequence converges to [", end="")
            for j in range(n - 1):
                print(x[j], ",", end="")
            print(x[n - 1], "]. Took", i + 1, "iterations.")
            return x
    print("Doesn't converge.")

