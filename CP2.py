import cv2
import numpy as np

'''Summary
This function must create a matrix
with the sizes suitable for matX
'''
def createMatrix(matX, coeficient = 2):
    matrix = np.ndarray((matX.size,matX.size))
    matrix.fill(0)
    return fillMatrix(matrix, coeficient)


'''
Fills matrix with our desired K 
to make the transformation similar to Caesar cipher
this specific K was chosen to show caesar cipher
essentially this creates an identity matrix nxn size multiplied 
by k our coeficcient for Caesar Cipher
'''
def fillMatrix(matrix, k):
    for i in range(0,len(matrix)):
        matrix[i,i] = k
    return matrix

'''
GramShmidt algorithms
'''
def gramShmidt(matV):
    if matV == 0:
        print("suck me")
        return
    height, width = matV.size()
    matU = np.ndarray(height, width)
    matU[0:, 0] = matV[0:, 0]/np.linalg.norm(matV[0:, 0])
    for iter in range(1, width):
        matU[0:, iter] = matV[0:, iter]
        for iter2 in range(1, height):
            matU[0:,iter] = matU[0:, iter]-(np.transpose(matU[0:,iter2])*matU[0:,iter])*matU[0:,iter2]
        matU[0:, iter] = matU[0:, iter]/np.norm(matU[0:, iter])

def transformTtoX(input):
    matrix = np.ndarray(len(input))
    if type(input) == str:
        for iter in range(0,len(input)):
            matrix[iter] = ord(input[iter])
    elif type(input) == np.ndarray:
        return input.flatten()
    return matrix

def transformXtoY(matX):
    chunk = 20
    matY = []
    iter = 1
    while iter*chunk*chunk < matX.size:
        matK = createMatrix(matX[(iter-1)*chunk*chunk:iter*chunk*chunk])
        matY.append(np.matmul(matX[(iter-1)*chunk*chunk:iter*chunk*chunk],matK))
        print(matX.size - iter*chunk*chunk)
        iter += 1
    if iter*chunk*chunk > matX.size:
        matK = createMatrix(matX[(iter-1)*chunk*chunk:])
        matY.append(np.matmul(matX[(iter-1)*chunk*chunk:],matK))

    return matY


'''
this function hides matK in matZ
and creates matZhat which is hidden from plain sight
'''
def transformZtoZhat(matY, matZ):
    pass


'''
This function changes the Least Significant Bit(LSB)
and encodes a message using stego
'''
def lsb(matZ = 0, matY = 0):
    testmat = []
    binMatY = []
    for submat in matY:
        for element in submat:
            binMatY.append(np.binary_repr(int(element), 9)) 
            testmat.append(element)
        
    print(testmat)
    print(binMatY)


'''
This function encrypts the data using a Caesar cipher
'''
def encryption(input):
    matX = transformTtoX(input)#fllaten function flattens the whole input
    matY = transformXtoY(matX)
    matZhat = lsb(0, matY)



if __name__ == '__main__':
    input = "me var texti" #v2.imread("new_img.jpg")
    encryption(input)

