import cv2
import numpy as np
import random

def encryption(input):
    return encryptionUsingK(input)

def createNxNMatrix(n):
    return fillMatrixInteger(np.ndarray((n,n)))

def fillMatrixInteger(matrix):
    height = len(matrix)
    width = len(matrix[0])
    for x in range(0, height):
        for y in range(0, width):
            matrix[x][y] = random.randint(0,500) 

    return matrix

def fillMatrixFloat(matrix):
    height = len(matrix)
    width = len(matrix[0])
    for x in range(0, height):
        for y in range(0, width):
            matrix[x][y] = random.uniform(0,200)

    return matrix


def encryptionUsingK(matrixT):
    type(matrixT)
    width = len(matrixT)
    matrixK = createNxNMatrix(matrixT.shape[1])
    blue, green, red = matrixT[0:,0:,0], matrixT[0:,0:,1], matrixT[0:,0:,2]
    matrixY = np.ndarray((matrixT.shape[0], matrixT.shape[1], 3))


    matrixY[0:,0:,0] = np.matmul(blue, matrixK)
    matrixY[0:,0:,1] = np.matmul(green, matrixK)
    matrixY[0:,0:,2] = np.matmul(red, matrixK)
    
    cv2.imwrite("file.jpg",matrixY)


    return matrixY


def matrixDeterminant(matrix):
    pass

def matrixInverse(matrix):
    pass

def richardson():
    pass

def gramSchmidtt(matV):
    height, width = matV.size()
    matU = np.ndarray(height, width)
    matU[0:, 0] = matV[0:, 0]/np.linalg.norm(matV[0:, 0])
    for iter in range(1, width):
        matU[0:, iter] = matV[0:, iter]
        for iter2 in range(1, height):
            matU[0:,iter] = matU[0:, iter]-(np.transpose(matU[0:,iter2])*matU[0:,iter])*matU[0:,iter2]
        matU[0:, iter] = matU[0:, iter]/np.norm(matU[0:, iter])


if __name__ == '__main__':
    input = cv2.imread("new_img.jpg")
    print(encryption(fillMatrixInteger(input)))







def randomShittyAlgorithmforHW():
    pass