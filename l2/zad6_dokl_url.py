import numpy as np

mA = np.array([[3.50, 2.77, -0.76, 1.80], [-1.80, 2.68, 3.44, -0.09], [0.27, 5.07, 6.90, 1.61], [1.71, 5.45, 2.68, 1.71]])
b = np.array([7.31, 4.23, 13.85, 11.55])
x = np.linalg.solve(mA, b)
print('[x1, x2, x3, x4] =', x)

det_mA = np.linalg.det(mA)
mA_inv = np.linalg.inv(mA)
print('det(A) =', det_mA)

l_mA = mA.tolist()
l_mA_inv = mA_inv.tolist()

l1 = []
l2 = []
for i in range(4):
    s_A = sum(abs(element) for element in l_mA[i])
    s_A_inv = sum(abs(element) for element in l_mA_inv[i])
    l1.append(s_A)
    l2.append(s_A_inv)

norma_A = max(l1)
norma_A_inv = max(l2)
print('||A|| =', norma_A)
print('||A^-1|| =', norma_A_inv)
print('cond(A) =', norma_A * norma_A_inv)
print(np.linalg.cond(mA, np.inf))
print('A @ x =', mA @ x)        # zgadza się z wektorem b
