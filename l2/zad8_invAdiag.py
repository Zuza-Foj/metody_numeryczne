import numpy as np

mA = np.array([[2, -1, 0, 0, 0, 0], [-1, 2, -1, 0, 0, 0], [0, -1, 2, -1, 0, 0], [0, 0, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 5]])
det_mA = np.linalg.det(mA)
print('det(A) =', det_mA)
cond_mA = np.linalg.cond(mA)
print('cond(A) =', cond_mA)
'''Wyznacznik jest okej, macierz nieosobliwa, czyli
możemy szukać macierzy odwrotnej. Pondto liczymy K(A),
wyszedł bliski jedności, zatem zadanie jest dobrze
uwarunkowane.'''

inv_mA = np.linalg.inv(mA)
print(inv_mA)
'''Macierz A^{-1} nie jest trójdiagonalna.'''
