import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 6, 400)

z1 = []
z2 = []
f_exp = []
for i in x:
    e_z1 = (6 - 2*i)/(6 + 4*i + i**2)
    z1.append(e_z1)
    e_z2 = (6 - 4*i + i**2)/(6 + 2*i)
    z2.append(e_z2)
    f_exp.append(np.exp(-i))

b_z1 = []
b_z2 = []
for i in range(len(z1)):
    b_z1.append(z1[i] - f_exp[i])
    b_z2.append(z2[i] - f_exp[i])

plt.figure(figsize=(12, 5))
plt.plot(x, z1, '--', label='Padé z1')
plt.plot(x, z2, '--', label='Padé z2')
plt.plot(x, f_exp, label='f(x)')
plt.title('Porównanie aproksymacji z exp(-x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()

'''Z tego co widzę, dla x bliskich zeru aproksymacje się sprawdzają.'''

fig0, (ax1, ax2) = plt.subplots(2, 1)
fig0.suptitle('Obie aproksymacje')
ax1.plot(x, z1, '-', label='Pade z1')
ax1.plot(x, f_exp, 'r', label='f(x)')
ax1.set_ylabel('z1')
ax2.plot(x, z2, '-', label='Pade z2')
ax2.plot(x, f_exp, 'r', label='f(x)')
ax2.set_xlabel('x')
ax2.set_ylabel('z2')
for ax in (ax1, ax2):
    ax.grid(True)
    ax.legend()
plt.show()

fig1, (ax3, ax4) = plt.subplots(1, 2)
fig1.suptitle('Błędy obu aproksymacji')
ax3.plot(x, b_z1, label='błąd ap. z1')
ax3.set_ylabel('błąd z1')
ax4.plot(x, b_z2, label='błąd ap.z2')
ax4.set_ylabel('błąd z2')
ax4.set_xlabel('x')
for ax in (ax3, ax4):
    ax.grid(True)
    ax.legend()
plt.tight_layout()
plt.show()

# zapisanie do pliku!!!!
