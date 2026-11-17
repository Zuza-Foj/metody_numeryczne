import numpy as np
import scipy.linalg as scipy
from gauss_jordan import gauss_jordan

mA = np.array([[2, -1, 0, 0, 0, 0], [-1, 2, -1, 0, 0, 0], [0, -1, 2, -1, 0, 0], [0, 0, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 5]])

print("własna implementacja:")
n = mA.shape[0]
I = np.eye(n)
A_inv_w = np.zeros((n, n))

for j in range(n):
    e_j = I[:, j]
    A_inv_w[:, j] = gauss_jordan(mA, e_j)
print("macierz odwrotna (własna):\n", A_inv_w)

print('biblioteka:')
det_mA = np.linalg.det(mA)
print('det(A) =', det_mA)
cond_mA = np.linalg.cond(mA)
print('cond(A) =', cond_mA)
'''Wyznacznik jest okej, macierz nieosobliwa, czyli
możemy szukać macierzy odwrotnej. Pondto liczymy K(A),
wyszedł bliski jedności, zatem zadanie jest dobrze
uwarunkowane.'''

inv_mA = np.linalg.inv(mA)
print("macierz odwrotna (biblioteka):\n", inv_mA)
'''Macierz A^{-1} nie jest trójdiagonalna.'''

print("\nRóżnica między metodami:", np.linalg.norm(A_inv_w - inv_mA))
