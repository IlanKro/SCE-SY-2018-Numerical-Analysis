import numpy as np
from scipy.linalg import solve_triangular as solve
from numpy.linalg import inv
from functools import reduce


class Matrix(object):
    def __init__(self, A, b=0):
        """
        creates a matrix and a solution vector for it.
        :param A: The matrix to construct
        :param b: The solution vector by default the vector is a vector of 0's
        """
        self.mat = np.array(A)
        self.b = np.array(0.0 for i in range(len(A))) if b == 0 else np.array(b)

    def __str__(self):
        newstr = ''
        for i in enumerate(self.mat):
            newstr += str(i[1]).replace(']', '|{}]\n'.format(self.b[i[0]]))
        return newstr

    @property
    def D(self):
        """
        Defines the diagonal(D) attribute of the matrix
        """
        diag = np.zeros_like(self.mat)
        for i in enumerate(self.mat):
            diag[i[0]][i[0]] = self.mat[i[0]][i[0]]
        return diag

    @property
    def U(self):
        """
        Defines the upper(U) attribute of the matrix
        """
        upper = np.zeros_like(self.mat)
        for i in enumerate(self.mat):
            for j in enumerate(self.mat):
                if i[0] < j[0]:
                    upper[i[0]][j[0]] = self.mat[i[0]][j[0]]
        return upper

    @property
    def L(self):
        """
        Defines the lower(L) attribute of the matrix
        """
        lower = np.zeros_like(self.mat)
        for i in enumerate(self.mat):
            for j in enumerate(self.mat):
                if i[0] > j[0]:
                    lower[i[0]][j[0]] = self.mat[i[0]][j[0]]
        return lower

    @staticmethod
    def check_invertible(A):
        """
            Checks if a matrix is invertible or not
            :return: boolean:True if it's invertible or False if it's singular
        """
        try:
            inv(A)
        except LinAlgError:
            return False
        return True

    def has_dominant_diag(self):
        """
        Checks if a matrix has a dominant diagonal
        :return: True if it does, False if it doesn't
        """
        for i in enumerate(self.mat):
            summ = reduce(lambda x, y: abs(x + y), i[1])
            current = abs(i[1][i[0]])
            summ -= current
            if summ > current:
                return False
        return True

    def cond(self):
        """
        Calculates the cond(A) of a matrix the formula is: normal(A)*normal(A^-1)
        :return: The value of condition A the bigger this value the less accurate the matrix will be.
        """

        def normal(A):
            return max(reduce(lambda x, y: abs(x + y), i) for i in A)
        return normal(self.mat) * normal(inv(self.mat)) if Matrix.check_invertible(self.mat) else "can't be inverted"

    def gauss_elemination(self, guess=[0, 0]):
        """
        Solves a matrix using gauss elemination method, prints the solution process
        :return: x a vector with the solutions for said matrix and solution vector
        """
        [A, b] = self.mat, self.b
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
                elemental_mat = elemental(index, i, len(A), multiplier)
                print("elemental matrix:", elemental_mat)
                A = elemental_mat.dot(A)
                b[index] = b[index] + (multiplier * float(b[i]))
                index = index + 1
            return [A, b]

        for i in range(len(A)):
            print('{})A:\n{}b:{}'.format(i + 1, A, b))
            [Ai, b] = biggest_value_swap(A, b, i, i)
            if not np.array_equal(Ai, A):  # So it doesn't print twice the same values
                print(') A:\n{0},\nb:{1}'.format(Ai, b))
            A = Ai
            [A, b] = gauss_scalling(A, b, i)
        print("Took {} iterations".format(i + 1))
        x = solve(A, b)  # solving triangular matrix.
        print("The result after solving a triangular scaled Matrix:{0}".format(x))
        return x

    def jacobi(self, guess,max_itr=1000, tol=0.0001):
        """
        "Jacobi's method: x[i](r+1)=b- sum((row members except i)*x[i](r)) i being the row, and r the guess number
        :param guess: the initial guess for this iterative method
        :param max_itr: max number of tolerable iterations (default 1000)
        :param tol: tolerance of how close the results are
        :return: the solution vector of the Matrix this method is used on.
        """
        x = guess
        n = len(self.mat)
        for k in range(max_itr):
            print("iteration number {}:".format(k + 1))
            old_x = x.copy()
            for i in range(n):
                sum1 = 0
                for j in range(n):
                    if (j!=i):
                        sum1 += self.mat[i][j] * x[j]
                print("x[{0}] = (1/{1})*({2} - {3})".format(i + 1, self.mat[i][i], self.b[i], sum1), end="" )
                x[i] = (1 / self.mat[i][i]) * (self.b[i] - sum1)
                print(" = {0}".format(x[i]))
            if len(list("ok" for index in range(n) if abs(x[index] - old_x[index]) < tol)) == n:
                print("took {} iterations".format(k + 1))
                return x
        print("The method didn't converge after {} iterations".format(max_itr))
        return x

    def gauss_seidel(self, guess,max_itr=1000,tol=0.0001):
        """
        Gauss_seidel's method: x[i](r+1)= b- sum((row members until i)*x[i](r+1))-sum((row  after i)*x[i](r)
        i being the row, and r the guess number
        :param guess: the initial guess for this iterative method
        :param max_itr: max number of tolerable iterations (default 1000)
        :param tol: tolerance of how close the results are
        :return: the solution vector of the Matrix this method is used on.
        """
        x = guess
        n = len(self.mat)
        for k in range(max_itr):
            print("iteration number {}:".format(k+1))
            old_x=x.copy()
            for i in range(n):
                sum1 = 0
                for j in range(i):
                    sum1 += self.mat[i][j] * x[j]
                sum2 = 0
                for j in range(n - 1, i, -1):
                    sum2 += self.mat[i][j] * x[j]
                print("x[{0}] = (1/{1})*({2} - {3} - {4})".format(i + 1, self.mat[i][i], self.b[i], sum1, sum2), end="")
                x[i] = (1 / self.mat[i][i]) * (self.b[i] - sum1 - sum2)
                print(" = {0}".format(x[i]))
            if len(list("ok" for index in range(n) if abs(x[index] - old_x[index]) < tol)) == n:
                print("took {} iterations".format(k+1))
                return x
        print("The method didn't converge after {} iterations".format(max_itr))
        return x

    def sor(self,w, guess,max_itr=1000,tol=0.00001):
        """
            A variation of Gauss Seidel method that uses a w constant in a a way that would make the
            main diagonal of the matrix a dominant diagonal for faster convention.
            w should be a number between 0 and 2 (not including)
            if w is 1 this methoid is essentially the same as gauss seidel method
            :param w: the constant on which this method is based should be between 0 and 2 not including.
            :param guess: the initial guess for this iterative method
            :param max_itr: max number of tolerable iterations (default 1000)
            :param tol: tolerance of how close the results are
            :return: the solution vector of the Matrix this method is used on.
        """
        if (w<=0 or w>=2):
            return "w out of range"
        a=self.D +w*self.L
        b=w*self.b
        c=w*self.U + (1-w)* self.D
        print ("SOR of this equation list can be represented as:\n{}x={}-{}x".format(a,b,c))
        x = guess
        n = len(self.mat)
        for k in range(max_itr):
            print("iteration number {}:".format(k + 1))
            old_x = x.copy()
            for i in range(n):
                sum1 = 0
                for j in range(i):
                    sum1 += self.mat[i][j] * x[j]
                sum2 = 0
                for j in range(n - 1, i, -1):
                    sum2 += self.mat[i][j] * x[j]
                print("x[{0}] = (1-{5})*x[{0}] ({5}/{1})*({2} - {3} - {4})".format(i + 1, self.mat[i][i], self.b[i], sum1, sum2,w), end="")
                x[i] = (1-w)*x[i] + (w / self.mat[i][i]) * (self.b[i] - sum1 - sum2)
                print(" = {0}".format(x[i]))
            if len(list("ok" for index in range(n) if abs(x[index] - old_x[index])<tol))==n:
                print("took {} iterations".format(k + 1))
                return x
        print("The method didn't converge after {} iterations".format(max_itr))
        return x

B = Matrix([[16, 3], [7, 11]], (11, 13))
print (list(i for i in range(3) if 1-1<2))
print(B.gauss_seidel([1, 2]))
print(B.jacobi([1, 2]))
print(B.sor(1.15,[1,2],100))