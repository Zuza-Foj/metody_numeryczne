import numpy as np

def gauss_jordan(mA, b, tol=1e-12):
    """Rozwiązuje układ A x = b metodą Gaussa-Jordana z wyborem elementu głównego."""
    n = len(b)
    mAb = np.hstack([mA.astype(float), b.astype(float).reshape(n, 1)])

    for k in range(n):
        wiersz_glowny = k + np.argmax(np.abs(mAb[k:, k]))
        if abs(mAb[wiersz_glowny, k]) < tol:
            raise ValueError('Macierz osobliwa (lub prawie osobliwa) - brak jednoznacznego rozwiązania.')
        if wiersz_glowny != k:
            mAb[[k, wiersz_glowny]] = mAb[[wiersz_glowny, k]]1
        mAb[k] = mAb[k] / mAb[k, k]
        for i in range(n):
            if i != k:
                mAb[i] = mAb[i] - mAb[i, k] * mAb[k]
    return mAb[:, n]

if __name__ == "__main__":
    x = [1, 2, 3]