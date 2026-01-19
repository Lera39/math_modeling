import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from scipy.integrate import odeint

t=np.arange(0, 4, 0.01)

def V(k, t):
    sk=t
    return sk
k0=1
kol=odeint(V, k0, t)
plt.plot(t, kol)
plt.axis('equal')
plt.savefig('fig_1.png')


