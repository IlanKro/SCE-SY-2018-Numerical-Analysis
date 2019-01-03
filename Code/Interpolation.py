import numpy as np
def results_into_matrix(results):
    """
    A function that makes a matrix based on data from a table
    :param results: a list of pairs of tuples
    :return: a matrix and a solution vector to represent the results numpy objects
    """
    A=np.array(np.identity(len(results)))
    b=np.array([0.0 for i in range(len(results))])
    deegre=len(results)
    for i in range(len(results)):
        temp_deegre=deegre-1
        for j in range(len(results)):
            A[i][j]= results[i][0]**temp_deegre
            print("a{2}*{0}^{1}".format(A[i][j],str(temp_deegre),j+1), end=" ")
            temp_deegre-=1
        print("\n")
        b[i]=results[i][1]
    return [A,b]

print (results_into_matrix([(1,10.5),(3,6.1),(5,3.5)]))
