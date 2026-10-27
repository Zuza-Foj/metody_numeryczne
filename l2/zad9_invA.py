import numpy as np

mA = np.array([[1, 3, -9, 6, 4], [2, -1, 6, 7, 1], [3, 2, -3, 15, 5], [8, -1, 1, 4, 2], [11, 1, -2, 18, 7]])
det_mA = np.linalg.det(mA)
print('wyznacznik mac. A:', det_mA)

try:
    A_inv = np.linalg.inv(mA)
    print('A_inv =\n', A_inv)
except np.linalg.LinAlgError as blad:
    print('Błąd:', blad)

'''Wyznacznik jest tak mały, że komputer
intrepretuje go jako '0', czyli macierz jest osobliwa,
nie da się jej odwrócić.'''
