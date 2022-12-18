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

    #print(list)
    return list

def transformXtoY(matX):
    chunk = 20
    matY = []
    iter = 1

    while iter*chunk*chunk < len(matX):
        matK = createMatrix(matX[(iter-1)*chunk*chunk:iter*chunk*chunk])
        matY.append(np.matmul(matX[(iter-1)*chunk*chunk:iter*chunk*chunk],matK))
        #print(matX.size - iter*chunk*chunk)
        iter += 1

    if iter*chunk*chunk > len(matX):  
        matK = createMatrix(matX[(iter-1)*chunk*chunk:])
        something = np.matmul(matX[(iter-1)*chunk*chunk:],matK)
        matY.append(something)

    return listFlatten(matY)

def listFlatten(lst):
    retLst = []
    for sub in lst:
        for element in sub:
            retLst.append(element)
    return retLst



'''
This function changes the Least Significant Bit(LSB)
and encodes a message using stego
'''
def lsb(matZ, matY):
    bool = False
    strIter = 1
    lstIter1 = 0
    binMatZ = binaryTransform(matZ)
    binMatY = (binaryTransform(matY))
    print(binMatY)
    print(binMatZ[0:14])
    for k in range(len(binMatZ)):

        if lstIter1 < len(binMatY):
            if strIter * 3 > len(binMatY[lstIter1]):
                strIter = 1
                lstIter1 += 1
                if lstIter1  == len(binMatY):
                    lstIter1 -= 1
                    bool = True

            if k <= len(binMatY)*4:
                binMatZ[k] = binMatZ[k][:-3]
                binMatZ[k] +=  binMatY[lstIter1][(strIter-1)*3:strIter*3]
                strIter += 1

            if bool == True:
                lstIter1 += 1

        else:
            binMatZ[k] = binMatZ[k][:-3]
            binMatZ[k] += "000"
    
    print(binMatZ[0:14])
    return binMatZ

def unflatten(mat, width = 0):
    list = []
    newlist = []
    height = 1
    if width == 0:
        width = mat[-1]
        mat = mat[:-1]

    for i in range(0, len(mat), 3):
        list.append([mat[i], mat[i+1], mat[i+2]])

        if i + 3 == (3*width*height):
            newlist.append(list)
            height += 1
            list = []

    return np.array(newlist)



def binaryTransform(lst):
    binMat = []
    for element in lst:
       binMat.append(bin(int(element), 12)) 

    return binMat

def decimalTransform(lst):
    decimalMat = []
    for element in lst:
       decimalMat.append(int(element,2)) 

    return decimalMat

def extractYfromZ(lst):
    length = len(lst) - 1
    binaryLst = binaryTransform(lst)
    tempLst = ""
    retLst = []
    '''while length > 0:
        if binaryLst[length][-3:] != "000":
            for i in range(length):
                if i % 4 == 0:
                    tempLst += binaryLst[i][-3:]
                    retLst.append(tempLst)
                    tempLst = []
                else:
                    tempLst += binaryLst[i][-3:]

        length -= 1
    '''
    print(binaryLst[0:14])
        
    return retLst

    return "error"

def extractXfromY(lst, k):
    ##this part of the code only workd for K matrox = k constant * I identity(nxn)
    chunk = 20
    width = int(lst[-1],2)
    lst = decimalTransform(lst[:-1])
    matX = []
    iter = 1

    while iter*chunk*chunk < len(lst):
        matK = createMatrix(lst[(iter-1)*chunk*chunk:iter*chunk*chunk], 1/k)
        matX.append(np.matmul(lst[(iter-1)*chunk*chunk:iter*chunk*chunk],matK))
        #print(matX.size - iter*chunk*chunk)
        iter += 1

 
    matK = createMatrix(lst[(iter-1)*chunk*chunk:], 1/k)
    something = np.matmul(lst[(iter-1)*chunk*chunk:], matK)
    matX.append(something)

    matX = listFlatten(matX)
    
    if width == 3:
        return matX

    else:
        print(width)
        return unflatten(matX, width)




def decrypt(image, k):
    image = image.flatten()
    lstY = extractYfromZ(np.ndarray.tolist(image))
    if lstY == "error":
        return -1
    print(lstY)
    lstX = extractXfromY(lstY, k)

    return lstX



'''
This function encrypts the data using a Caesar cipher
'''
def encryption(input):
    matX = transformTtoX(input)
    matY = transformXtoY(matX)
    imgZ = cv2.imread("DOG.JPG")
    widthZ = len(imgZ[0])
    imgZ = imgZ.flatten()
    listZ = np.ndarray.tolist(imgZ)
    matZhat = lsb(listZ, matY)
    matZhat = decimalTransform(matZhat)
    matZhat = unflatten(matZhat, widthZ)
    cv2.imwrite("file.jpg", matZhat)



if __name__ == '__main__':
    input = "me"#cv2.imread("new_img.jpg")
    encryption(input)
    input = cv2.imread("file.jpg")
    decrypted = decrypt(input, 2)
    print(decrypted[0:4])
    cv2.imwrite("decrypted.jpg", decrypted)
    

    
    

