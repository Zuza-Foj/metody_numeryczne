import numpy as np

'''Wyliczyłam a0 z pierwszego punktu [0, -1], a0 = -1.'''

p = [[0, -1], [1, 1], [3, 3], [5, 2], [6, -2]]

x = []
y = []
for i in p:
    y.append(i[1])
    x.append([1, i[0], i[0]**2, i[0]**3, i[0]**4])
print(y, x)

m_A = np.array(x)
b = np.array(y)

a = np.linalg.solve(m_A, b)
print('[a0, a1, a2, a3, a4] =', a.tolist())


