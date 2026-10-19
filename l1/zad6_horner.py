import numpy as np
import time

x = np.linspace(-10, 10, 200001)
t0 = time.perf_counter()
w = (((6*x + 5)*x - 13)*x + 1)*x + 1
print("NumPy, Horner:", time.perf_counter() - t0)
t0_2 = time.perf_counter()
w_2 = 6 * x ** 4 + 5 * x ** 3 - 13 * x ** 2 + x + 1
print("NumPy, wielomian:", time.perf_counter() - t0_2)

