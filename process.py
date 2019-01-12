import sys
print(sys.version)

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from scipy import signal

num = [1]
den = [30, 5]
dt = 0.1
dis = signal.cont2discrete(([num], den), dt=dt)
P = signal.dlti(dis[0], dis[1], dt=dt).to_ss()
print(P)
# step = P.step()
# plt.plot(step[0], step[1][0])
# plt.show()
A = P.A
B = P.B
C = P.C
D = P.D
# o = P.output([1, 1], [0, 10], x0=[0.1])
# plt.plot(o[0], o[1])
# plt.show()

x = np.array([0])
u = np.array([1])

def step(A, B, C, D, x, u):
	x1 = A*x + B*u
	y = C*x + D*u
	return [x1, y]

T = 100
value = np.arange(0, T, 1, dtype=np.float64)
time = np.arange(0, T, 1, dtype=np.float64)
for i in range(T):
	[x, y] = step(A, B, C, D, x, u)
	y = y[0,0]
	value[i] = y

plt.plot(time, value)
plt.show()
