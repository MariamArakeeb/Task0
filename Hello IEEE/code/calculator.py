import numpy as np

def matsum(arr1,arr2):
    arr1= np.array(arr1)
    arr2= np.array(arr2)
    return arr1+arr2

def matsub(arr1,arr2):
    arr1= np.array(arr1)
    arr2= np.array(arr2)
    return arr1-arr2

def matmul(arr1,arr2):
    arr1= np.array(arr1)
    arr2= np.array(arr2)
    return np.dot(arr1,arr2)

def scalarsum(scalar,arr):
    arr= np.array(arr)
    return arr+ scalar

def scalarsub(scalar,arr):
    arr= np.array(arr)
    return arr- scalar

def matnorm(arr):
    arr= np.array(arr,dtype=float)
    MaxVal=np.max(arr)
    MinVal=np.min(arr)
    
    if MaxVal== MinVal :
        raise ValueError("can't normalise constant matrix")
        
    Norm= (arr- MinVal)/ (MaxVal-MinVal)
    return Norm

def Main():
    
    A = [[1, 2],
         [3, 4]]
    
    B = [[5, 6],
         [7, 8]]
    
    print(" A:\n", np.array(A))
    print(" B:\n", np.array(B))
    
    print("A + B:\n", matsum(A, B))
    print("A - B:\n", matsub(A, B))
    print("A * B:\n", matmul(A, B))
    print("A +5: \n", scalarsum(5, A))
    print("A -5: \n ", scalarsub(5, A))
    print("the normalization of A: \n", matnorm(A))
    
Main()
"""
Spyder Editor

This is a temporary script file.
"""

