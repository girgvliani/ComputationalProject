import cv2
import numpy as np

'''Summary
This function must create a matrix
with the sizes suitable for matX
'''
def createMatrix(matX, k = 2):
    return fillMatrix(np.ndarray((matX.size,matX.size)), k)


'''
Fills matrix with our desired K 
to make the transformation similar to Caesar cipher
this specific K was chosen to show caesar cipher
essentially this creates an identity matrix nxn size multiplied 
by k our coeficcient for Caesar Cipher
'''
def fillMatrix(matrix, k):
    for i in range(0,149):
        matrix[i,i] = k
    return matrix

'''
GramShmidt algorithms
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

def TtoX(input):
    matrix = np.ndarray(len(input))
    if input.type == str:
        for iter in range(0,input):
            matrix[iter] = input[iter]
    return matrix

def XtoY(matX):
    chunk = 150
    matY = []
    iter = 1
    while iter*chunk*chunk < matX.size:
        matK = createMatrix(matX[(iter-1)*chunk*chunk:iter*chunk*chunk])
        matY.append(np.matmul(matX[(iter-1)*chunk*chunk:iter*chunk*chunk],matK))
        print(matX.size - iter*chunk*chunk)
        iter += 1
    if iter*chunk*chunk > matX.size:
        matK = createMatrix(matX[(iter-1)*chunk*chunk:])
        matY.append(np.matmul(matX[(iter-1)*chunk:],matK))

    return matY


'''
This function encrypts the data using a Caesar cipher
'''
def encryption(input):
    matX = TtoX(input)#fllaten function flattens the whole input
    print(matX)
    print(XtoY(matX))



if __name__ == '__main__':
    input = "image"#cv2.imread("new_img.jpg")
    encryption(input)

