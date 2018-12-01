import numpy as np
from numpy.linalg import inv
from scipy.linalg import solve_triangular as solve
def make_matrix(A):
    """Makes a desired matrix to work with numpy"""
    return np.array(A)

def cond(A):
    """Calculates the cond(A) of a matrix normal(A)*normal(A^-1)
    :param: A matrix to check cond(A) in
    :return: The value of condition A the bigger this value the less accurate the matrix will be.
    """
    def normal(A):
       sum = 0
       maxSum = 0
       for i in A:
            for j in i:
               sum += abs(j)
            if sum > maxSum:
                maxSum = sum
            sum=0
       return maxSum
    return normal(A) * normal(inv(A))
def check_singularity(A):
    """Checks if a matrix is singular or not
        :param: A the matrix to check
        :return: boolean:True if it's invertuible or False if it's singular
    """
    try:
        inv(A)
    except str:
        return False
    return True


def gauss_elemination_method(A,b):
    """Insert a matrix and a solution vector, and you will get a print of gauss scalling and a solution
    :param: A an invertible matrix n*n
    :param: b the solution vector (needs to be same length as n)
    :return: x a vector with the solutions for said matrix and solution vector
    """
    def biggest_value_swap(A, b, i, j):

        def switch_lines(A, l1, l2):
            B = np.identity(len(A))
            B[l1][l1] = 0
            B[l1][l2] = 1
            B[l2][l2] = 0
            B[l2][l1] = 1
            return B.dot(A)

        maximum = A[i][j]
        index = i
        biggest_index = i
        while index < len(A):
            if abs(A[index][j]) > maximum:
                maximum = abs(A[index][j])
                biggest_index = index
            index = index + 1
        if A[biggest_index][j] == 0:
            return 'error'
        b[biggest_index], b[i] = b[i], b[biggest_index]
        return [switch_lines(A, i, biggest_index), b]

    def gauss_scalling(A, b, i):
        def elemental(i, j, n, val):
            """Makes an elementary matrix in size of n*n"""
            A = np.identity(n)
            A[i][j] = val
            return A

        index = i + 1
        while index < len(A):
            multiplier = -1 * (A[index][i] / A[i][i])
            A = elemental(index, i, len(A), multiplier).dot(A)
            b[index] = b[index] + (multiplier * float(b[i]))
            index = index + 1

        matrix = [A, b]
        return matrix
    for i in range(0,len(A)):
        print('A:\n{0},\nb:{1}'.format(A, b))
        [A, b] = biggest_value_swap(A, b, i, i)
        print('A:\n{0},\nb:{1}'.format(A, b))
        [A, b] = gauss_scalling(A, b, i)
    x=solve(A,b)
    return x



