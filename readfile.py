import numpy as np
import io
''' 
Open, access, print, and close a text file
'''
__train_file = open("traindata.txt", "rt")
#print(__train_file.readable())
#print(__train_file.read())
__train_file.close()

'''
Open file as matrix with labels still inside. Then separate labels into separate matrices
'''

file_Array = np.genfromtxt("traindata.txt", dtype = str)
file_Matrix = np.asmatrix(file_Array)
tSize = file_Matrix.shape
data_Matrix = (file_Matrix[1:tSize[0],1:tSize[1]]).astype(np.float)
rlabel_Matrix = file_Matrix[1:tSize[0],0]
clabel_Matrix = file_Matrix[0,1:tSize[1]]
print(tSize)
print(data_Matrix)
print(rlabel_Matrix)
print(clabel_Matrix)


#print(data_Matrix[1,:])


