import cv2
import numpy as np

'''Summary
This function must create a matrix
with the sizes suitable for matX
'''
def createMatrix(matX, k = 2):
    return fillMatrix(np.ndarray(matX.size), k)


'''
Fills matrix with our desired K 
to make the transformation similar to Caesar cipher
'''
def fillMatrix(matrix, k):
    for element in range(0,matrix.size):
        matrix[element] = k
    return matrix

'''
gramShmidt algorithms
'''
def gramShmidt(matV):
    height, width = matV.size()
    matU = np.ndarray(height, width)
    matU[0:, 0] = matV[0:, 0]/np.linalg.norm(matV[0:, 0])
    for iter in range(1, width):
        matU[0:, iter] = matV[0:, iter]
        for iter2 in range(1, height):
            matU[0:,iter] = matU[0:, iter]-(np.transpose(matU[0:,iter2])*matU[0:,iter])*matU[0:,iter2]
        matU[0:, iter] = matU[0:, iter]/np.norm(matU[0:, iter])


'''
This function encrypts the data using a Caesar cipher
'''
def encryption(input):
    matX = input.flatten()#flaten function flattens the whole input
    print(matX)
    matK = createMatrix(matX)##TODO following code is not correct just for testing
    print(matK)
    print(matX+matK)



if __name__ == '__main__':
    input = cv2.imread("new_img.jpg")
    encryption(input)

