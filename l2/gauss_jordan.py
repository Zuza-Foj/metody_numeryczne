import numpy as np
import scipy.linalg as scipy

def gauss_jordan(mA, b):
    mA = np.array(mA, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    for k in range(n - 1):
        max_row = np.argmax(np.abs(mA[k:, k])) + k
        if mA[max_row, k] == 0:
            raise ValueError("Macierz jest osobliwa.")
        if max_row != k:
            mA[[k, max_row]] = mA[[max_row, k]]
            b[[k, max_row]] = b[[max_row, k]]
        for i in range(k + 1, n):
            factor = mA[i, k] / mA[k, k]
            mA[i, k:] -= factor * mA[k, k:]
            b[i] -= factor * b[k]
    if mA[n - 1, n - 1] == 0:
        raise ValueError("Macierz jest osobliwa.")
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        suma = np.dot(mA[i, i + 1:], x[i + 1:])
        x[i] = (b[i] - suma) / mA[i, i]
    return x

if __name__ == "__main__":
    A_test = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
    b_test = np.array([8, -11, -3])
    x_moj = gauss_jordan(A_test, b_test)
    x_scipy = scipy.solve(A_test, b_test)


    print("Rozwiązanie (własne):", x_moj)
    print("Rozwiązanie (SciPy): ", x_scipy)
    print("Różnica (norma błędu):", np.linalg.norm(x_moj - x_scipy))

