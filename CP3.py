import numpy as np

"""
sovlves using normal EQ
"""
def normalEQ(matA, b):
    x = []
    transA = transposedMat(matA)
    aTA = np.matmul(transA, matA)
    print(aTA)
    aTb = np.matmul(transA, b)
    aTAinv = inverseMat(aTA)
    x = np.matmul(aTAinv, aTb)
    return x

'''
solves the EQ using QR factorization
'''
def qRFactorization():
    pass

'''
We are using Hausholder Transformation
'''
def hausholderTransformation():
    pass

'''
name of this fucntion is self explanatory
'''
def modifiedGramSchmidtt():
    pass

'''
This function solves the problem using least squared problem using NORMAL EQ and QR FACTORIZATION 
'''
def lLS():
    print("I am working")
    pass

'''
We need to check orthogaonality of Q matrix in QR decompositon
'''
def orthogonalCheck():
    pass



def inverseMat(mat):
    if np.linalg.det(mat) == 0:
        print("Can not calculate the inverse: determinant of the matrix = 0")
        return -1
        #raise Exception("Can not calculate the inverse: determinant of the matrix = 0" )
    return np.linalg.inv(mat)

'''
transposed matrix if I have time I will write my own code 
to change the matrix
'''
def transposedMat(mat):
    return np.transpose(mat)


"""
this function is/was for testing if one wants to test the code
please use this function and don't change the code anywhere else
"""
def testing():
    #print(inverseMat(np.array([[21,28],
     #                           [28,38]])))
    print(normalEQ(np.array([[1,2],
                    [2,3],
                    [4,5]]), [3,5,9]))

if __name__ == '__main__':
    testing()