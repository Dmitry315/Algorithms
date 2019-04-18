import cmath
import numpy as np
import matplotlib.pyplot as plt
j = cmath.sqrt(-1)

def real_dzeta(a, x):
    return sum([1/cmath.exp(np.log(i) * (a + x*j)) for i in range(1,200)]).real

def imag_dzeta(a, x):
    return sum([1/cmath.exp(np.log(i) * (a + x*j)) for i in range(1,200)]).imag

rng2 = np.arange(-20.0, 20.0, 0.01)

zero = np.array([-20.0,20.0])

plt.figure(1)
plt.subplot(311)
plt.title('0.9')
plt.plot(rng2, np.array([real_dzeta(0.6, i) for i in rng2]), 'k')
plt.plot(rng2, np.array([imag_dzeta(0.6, i) for i in rng2]), 'k')
plt.plot( zero, np.array([0.0,0.0]), 'k')

plt.subplot(312)
plt.title('0.5')
plt.plot(rng2, np.array([real_dzeta(0.5, i) for i in rng2]), 'k')
plt.plot(rng2, np.array([imag_dzeta(0.5, i) for i in rng2]), 'k')
plt.plot( zero, np.array([0.0,0.0]), 'k')

plt.subplot(313)
plt.title('0.1')
plt.plot(rng2, np.array([real_dzeta(0.4, i) for i in rng2]), 'k')
plt.plot(rng2, np.array([imag_dzeta(0.4, i) for i in rng2]), 'k')
plt.plot( zero, np.array([0.0,0.0]), 'k')

plt.show()
