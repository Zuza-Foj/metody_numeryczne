import numpy as np
from scipy.sparse import csr_matrix

def tridiag_martix(n):
    data = []
    indices = []
    indptr = []

    for i in range(n + 1):
        indices.extend([i - 1, i, i + 1])
        data.extend([-1, 4, -1])
        indptr.append(3 * i)

    A = csr_matrix((data, indices, indptr), shape=(n, n))
    return A.toarray()

print(tridiag_martix(12))




'''
append(i - 1, i, i + 1)
dla i = 0: n, 0, 1
dla i = 1: 0, 1, 2
dla i = 2: 1, 2, 3
dla i = 3: 2, 3, 4
.
.
.
dla i = n: n-1, n, n+1


0 1
0 1 2
1 2 3 
2 3 4
3 4

jak lista z indeksami jest pusta to dodajemy 1 na n-tym miejscu.'''