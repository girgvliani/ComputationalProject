import cv2
import numpy as np

'''Summary
This function must create a matrix
with the sizes suitable for matX
'''
def createMatrix(matX):
    pass

def gramShmidt(matV):
    height, width = matV.size()
    matU = np.ndarray(height, width)
    matU[0:, 0] = matV[0:, 0]/np.linalg.norm(matV[0:, 0])
    for iter in range(1, width):
        matU[0:, iter] = matV[0:, iter]
        for iter2 in range(1, height):
            matU[0:,iter] = matU[0:, iter]-(np.transpose(matU[0:,iter2])*matU[0:,iter])*matU[0:,iter2]
        matU[0:, iter] = matU[0:, iter]/np.norm(matU[0:, iter])

def encryption(input):
    matX = input.flatten()
    print(len(matX))
    matK = createMatrix(matX)##TODO following code is not correct just for testing
    print(np.matmul(matX,matK))



if __name__ == '__main__':
    input = cv2.imread("new_img.jpg")
    encryption(input)

