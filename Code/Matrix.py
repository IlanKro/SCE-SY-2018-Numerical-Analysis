import numpy as np
from scipy.linalg import solve_triangular as solve
from numpy.linalg import inv
class Matrix(object):
    def __init__(self,A,b=0):
        """
        creates a matrix and a solution vector for it.
        :param A: The matrix to construct
        :param b: The solution vector by default the vector is a vector of 0's
        """
        self.mat= np.array(A)
        self.D = np.zeros_like(A)
        self.diag()
        self.U= np.zeros_like(A)
        self.upper()
        self.L= np.zeros_like(A)
        self.lower()
        self.b=b
        if b==0:
            self.b=np.array( [0.0 for i in range(len(A))])
    def LU(self):
        """
            An algorithm to update the attributes of L,D,U  in case the attribute of A is changed.
        """
        self.diag()
        self.upper()
        self.lower()

    def diag(self):
        """
        Defines the diagonal(D) attribute of the matrix
        """
        for i in range (len(self.mat)):
            self.D[i][i]=self.mat[i][i]
    def upper(self):
        """
        Defines the upper(U) attribute of the matrix
        """
        for i in range(0,len(self.mat)):
            for j in range (0,len(self.mat)):
                if (i<j):
                    self.U[i][j] = self.mat[i][j]
    def lower(self):
        """
        Defines the lower(L) attribute of the matrix
        """
        for i in range(0,len(self.mat)):
            for j in range (0,len(self.mat)):
                if (i>j):
                    self.L[i][j] = self.mat[i][j]

    def check_invertible(self):
        """
            Checks the  matrix is invertible or not
            :return: boolean:True if it's invertible or False if it's singular
        """
        try:
            inv(A)
        except str:
            return False
        return True
    def has_dominant_diag(self):
        """
        Checks if a matrix has a dominant diagonal
        :return: True if it does, False if it doesn't
        """
        summ=0
        current=0
        for i in range(len(self.mat)):
            for j in range(len(self.mat)):
                if i==j:
                    current=abs(self.mat[i][i])
                else:
                    summ+=abs(self.mat[i][j])
            if (summ>current):
                return False
            summ=0
        return True
    def cond(self):
        """
        Calculates the cond(A) of a matrix the formula is: normal(A)*normal(A^-1)
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
                sum = 0
            return maxSum
        print("the inverted matrix is:\n",inv(self.mat))
        return normal(self.mat) * normal(inv(self.mat))

    def gauss_elemination(self):
        """
        Solves a matrix using gauss elemination method, prints the solution process
        :return: x a vector with the solutions for said matrix and solution vector
        """
        [A,b]=self.mat,self.b
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

        for i in range(0, len(A)):
            print('A:\n{0},\nb:{1}'.format(A, b))
            [A, b] = biggest_value_swap(A, b, i, i)
            print('A:\n{0},\nb:{1}'.format(A, b))
            [A, b] = gauss_scalling(A, b, i)
        x = solve(A,b)  # solving triangular matrix.
        return x
    def iterative_convergence(self,x,xI,tolerance):
        """
        checks if a loop using a vector as result needs to end or not calculating if 2 vectors are close enough, using their normals.
        :param x: Previous x (xr)
        :param xI: new x (xr+1)
        :param tolerance: the tolerance factor of the iteration
        :return: True if the iterative loop ended in success, False rhe loop needs to keep going.
        """
        if check_invertible() is False:
            return
        diff1norm = 0.0
        oldnorm = 0.0
        for i in range(len(self.b)):
            diff1norm = diff1norm + abs(x[i] - xI[i])
            oldnorm = oldnorm + abs(xI[i])
        if oldnorm == 0.0:
            oldnorm = 1.0
        norm = diff1norm / oldnorm
        if (norm < tolerance):
            return True
        return False


    def iterative(self,method,max_iter=10000,tolerance=0.00001):
        """
        Calculates a solution for a matrix and a solution vector using 2 methods
        that can be choosen when the function is called
        :param method: which method to use either "Jacobi" or "Gauss Seidel" are the only valid inputs
        :param max_iter: max number of iterations the default is 10000
        :param tolerance: tolerance of solution the default is 0.0001
        :return: either an error (in string) if something gone wrong an exception if the matrix ins't invertable,
        or the solution of the matrix and it's solution vector
        """
        [A,b]=self.mat,self.b
        def gauss_seidel(self):
            G = (-1 * inv(self.D + self.L)).dot(self.U)
            print("G:", G)
            H = inv(self.L + self.D)
            print("H:", H)
            return [G,H]
        def Jacobi(self):
            G =((-1 *inv(self.D)).dot(inv(self.L+self.U)))
            print("G:", G)
            H = inv(self.D)
            print("H:", H)
            return[G,H]
        iteration_num = 0
        x = np.zeros_like(self.b)
        x[0]=1
        if (method=="Jacobi"):
            [G,H]=Jacobi(self)
        elif (method == "Gauss Seidel"):
            [G,H]=gauss_seidel(self)
        else:
            return "Wrong input"
        xI=x
        while (iteration_num!=max_iter):
            xI= G.dot(x)+H.dot(self.b)
            iteration_num += 1
            print(iteration_num,")",x)
            if (Matrix.iterative_convergence(self,x,xI,tolerance)):
                print("number of Iterations:",(iteration_num))
                return x
            x = xI
            if x[0]>10e+33: #putting an upper limit so the solution doesn't go too high..
                return "does not converge"
        return "does not converge"

    def sor(self,w=1.5,max_iter=1000,tolerance=0.00001):
        """
        :param w: a variable between 0 and 2 (default is 1.5)
        :param  max_iter maximum iterations the code can go up to 1000 by default.
        :param tolerance: tolerance of solution the default is 0.0001
        :return: the solution to a matrix.
        """
        if (check_invertible() is False):
            return
        if (w<=0 or w>=2):
            return "Error, cannot initiate the function"
        x=np.zeros_like(self.b)
        x[0]=5  #don't want the initial vector to be all 0's but the actual guess doesn't matter much.
        xI=x
        iteration_num=0
        while(iteration_num!=max_iter):
            iteration_num+=1
            xI=(inv((self.D + w*self.L)).dot((1-w)*self.D - w * self.U)).dot(x) + (w * inv((self.D + w*self.L)).dot(self.b))#the sor formula
            print(iteration_num, ")", x)
            if (Matrix.iterative_convergence(self,x, xI, tolerance)):
                print("number of Iterations:", (iteration_num))
                return x
            x = xI
            if x[0] > 10e+33:  # putting an upper limit so the loop doesn't go too high.. needlessly
                return "does not converge"
        return "does not converge"


A= Matrix([[1,2],[2,1]],[0,1])
A.gauss_elemination()




