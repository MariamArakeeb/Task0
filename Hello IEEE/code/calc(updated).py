def matsum(arr1, arr2):
     sum = []
     for i in range(len(arr1)):
        row = []
        for j in range(len(arr1[0])):
            row.append(arr1[i][j] + arr2[i][j])
        sum .append(row)
     return sum

def matsub(arr1, arr2):
    sub = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr1[0])):
            row.append(arr1[i][j] - arr2[i][j])
        sub.append(row)
    return sub

def matmul(arr1, arr2):
    multiplicaton = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr2[0])):
            total = 0
            for k in range(len(arr2)):
                total += arr1[i][k] * arr2[k][j]
            row.append(total)
        multiplicaton.append(row)
    return multiplicaton

def scalarsum(scalar, arr):
    Ssum = []
    for i in range(len(arr)):
        row = []
        for j in range(len(arr[0])):
            row.append(arr[i][j] + scalar)
        Ssum.append(row)
    return Ssum


# -------------------------------
# Scalar Subtraction
# -------------------------------
def scalarsub(scalar, arr):
    Ssub = []
    for i in range(len(arr)):
        row = []
        for j in range(len(arr[0])):
            row.append(arr[i][j] - scalar)
        Ssub.append(row)
    return Ssub



def matnorm(arr):
    flat = []
    for row in arr:
        for value in row:
            flat.append(value)

    min_val = min(flat)
    max_val = max(flat)

    if max_val == min_val:
        raise ValueError("Cannot normalize matrix with constant values.")

    result = []
    for i in range(len(arr)):
        row = []
        for j in range(len(arr[0])):
            normalized_value = (arr[i][j] - min_val) / (max_val - min_val)
            row.append(normalized_value)
        result.append(row)

    return result



A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

print("A + B =", matsum(A, B))
print("A - B =", matsub(A, B))
print("A * B =", matmul(A, B))
print("A+5 =", scalarsum(5, A))
print("A-5 =", scalarsub(5, A))
print("Normalized A =", matnorm(A))


"""
Spyder Editor

This is a temporary script file.
"""

