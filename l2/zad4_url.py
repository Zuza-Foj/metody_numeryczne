import numpy as np

m_A = np.array([[0, 0, 2, 1, 2], [0, 1, 0, 2, -1], [1, 2, 0, -2, 0], [0, 0, 0, -1, 1], [0, 1, -1, 1, -1]])
b = np.array([1, 1, -4, -2, -1])

x = np.linalg.solve(m_A, b)
print('[x1, x2, x3, x4, x5] =', x.tolist())
