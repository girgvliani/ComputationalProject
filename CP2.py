import cv2
import numpy as np

'''Summary
This function must create a matrix
with the sizes suitable for matX
'''
def createMatrix(matX, coeficient = 2):
    matrix = np.ndarray((len(matX),len(matX)))
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
    height, width = matV.size()
    matU = np.ndarray(height, width)
    matU[0:, 0] = matV[0:, 0]/np.linalg.norm(matV[0:, 0])
    for iter in range(1, width):
        matU[0:, iter] = matV[0:, iter]
        for iter2 in range(1, height):
            matU[0:,iter] = matU[0:, iter]-(np.transpose(matU[0:,iter2])*matU[0:,iter])*matU[0:,iter2]
        matU[0:, iter] = matU[0:, iter]/np.norm(matU[0:, iter])

def transformTtoX(input):
    width = 0
    list = []

    if type(input) == str:
        stringIdentifier = 3
        for iter in range(0,len(input)):
            list.append(ord(input[iter]))
        list.append(stringIdentifier)

    elif type(input) == np.ndarray:
        width = len(input[0])
        input = input.flatten()
        list = np.ndarray.tolist(input)
        list.append(width)

    print(list)
    return list

def transformXtoY(matX):
    chunk = 20
    matY = []
    iter = 1

    while iter*chunk*chunk < len(matX):
        matK = createMatrix(matX[(iter-1)*chunk*chunk:iter*chunk*chunk])
        matY.append(np.matmul(matX[(iter-1)*chunk*chunk:iter*chunk*chunk],matK))
        print(matX.size - iter*chunk*chunk)
        iter += 1

    if iter*chunk*chunk > len(matX):  
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
def lsb(matZ, matY):
    print(matY)
    print(matZ)
    iter = 1
    iterz = 0
    binMatZ = binaryTransform(matZ)
    binMatY = (binaryTransform(matY))
    print(binMatY)
    for iter1 in range(len(binMatY)):
        iter = 1
        ##i Chose 3 to change last 3 bits only
        while iter*3 <= len(binMatY[iter1]):
            if iterz <= len(binMatZ):
                binMatZ[iterz] = binMatZ[iterz][:-2]
                binMatZ[iterz] +=  binMatY[iter1][(iter-1)*3:iter*3]     
                iter += 1
                iterz += 1
            else:
                binMatZ[iterz] = binMatZ[iterz][:-2]
                binMatZ[iterz] += '000'
                print(binMatZ[iterz])      
                iter += 1

    print(binMatZ)
        

def unflatten(mat):
    list = []
    newlist = []
    width = mat[-1]
    print(width)
    mat = mat[:-1]
    height = 1
    for i in range(0, len(mat), 3):
        list.append([mat[i], mat[i+1], mat[i+2]])

        if i + 3 == (3*width*height):
            newlist.append(list)
            height += 1
            list = []

    return np.array(newlist)



def binaryTransform(mat):
    binMatY = []
    for submat in mat:
        for element in submat:
            binMatY.append(np.binary_repr(int(element), 9)) 

    return binMatY

'''
This function encrypts the data using a Caesar cipher
'''
def encryption(input):
    matX = transformTtoX(input)
    matY = transformXtoY(matX)
    widthZ = len(cv2.imread("svaneti.JPG")[0])
    listZ = np.ndarray.tolist(cv2.imread("svaneti.JPG").flatten())
    listZ.append(widthZ)
    matZhat = lsb(listZ, matY)



if __name__ == '__main__':
    input = "me"#cv2.imread("new_img.jpg")
    print(input)
    encryption(input)
   

    '''
    width = len(input[0])
    input = input.flatten()
    list = np.ndarray.tolist(input)
    list.append(width)
    encryption(list)
    cv2.imwrite("file.jpg",unflatten(list))
    '''
    

