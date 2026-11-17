import numpy as np
from gauss_jordan import gauss_jordan

mA = np.array([[1, 3, -9, 6, 4], [2, -1, 6, 7, 1], [3, 2, -3, 15, 5], [8, -1, 1, 4, 2], [11, 1, -2, 18, 7]])
det_mA = np.linalg.det(mA)
print('det(A):', det_mA)

n = mA.shape[0]
I = np.eye(n)
A_inv_w = np.zeros((n, n))

try:
    for j in range(n):
        A_inv_w[:, j] = gauss_jordan(mA, I[:, j])
    print("Macierz odwrotna (własna):\n", A_inv_w)
except ValueError as e:
    print("Własna funkcja zatrzymała się:", e)

'''Własna funkcja zwraca wartości rzędu 10^15, ponieważ w trakcie eliminacji Gaussa wskutek błędów zaokrągleń 
na przekątnej zamiast dokładnego zera pojawia się resztka numeryczna rzędu 10^-16. 
Macierz odwrotna jest bezużyteczna!'''

try:
    A_inv = np.linalg.inv(mA)
    print('A_inv =\n', A_inv.tolist())
except np.linalg.LinAlgError as blad:
    print('Błąd:', blad)

'''Wyznacznik jest tak mały, że komputer
intrepretuje go jako '0', czyli macierz jest osobliwa,
nie da się jej odwrócić.'''
