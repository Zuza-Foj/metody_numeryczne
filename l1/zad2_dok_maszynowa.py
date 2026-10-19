import numpy as np
import sys

# empirycznie
eps = 1.0
while 1.0 + eps / 10.0 > 1.0:
    eps = eps / 10.0

print("Dokładność maszynowa (float64), obliczona pętlą:", eps)

# f. wbudowana
print("sys.float_info.epsilon:", sys.float_info.epsilon)
print("np.finfo(np.float64).eps:", np.finfo(np.float64).eps)

'''Generalnie się zgadza. W internecie napisano, że:
Dla standardowego komputera z arytmetyką IEEE 754 wynik nie zależy od procesora, 
tylko od formatu liczby. '''
