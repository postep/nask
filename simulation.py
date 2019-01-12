import sys
print(sys.version)

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from scipy import signal

NUM = [1]
DEN = [30, 5]
DT = 0.1
START = 0

class Process():
	def __init__(self):
		dsys = signal.cont2discrete((NUM, DEN), dt=DT)
		P = signal.dlti(dsys[0], dsys[1], dt=DT).to_ss()
		self.A = P.A
		self.B = P.B
		self.C = P.C
		self.D = P.D
		self.x = np.array([START])
		self.y = START
		

	def next_step(self, u):
		u = np.array([u])
		
		self.x = self.A*self.x + self.B*u
		y = self.C*self.x + self.D*u
		self.y = y[0,0]
		
		return [self.x[0,0], self.y]


class Controller:
	def __init__(self, kp, ki, kd):
		self.kp = kp
		self.ki = ki
		self.kd = kd
		self.u = 0
		self.u_1 = 0
		self.e = 0
		self.e_1 = 0
		self.e_2 = 0

	def next_step(self, e):
		self.e_2 = self.e_1
		self.e_1 = self.e
		self.e = e
		self.u_1 = self.u

		Ti = self.kp/self.ki
		Td = self.kd/self.kp
		self.u = self.u_1 + self.kp*((1+DT/Ti+Td/DT)*e + 
			(-1-2*Td/DT)*self.e_1 + Td*self.e_2/DT)

		return self.u


def test_process(p):
	T = 300
	value = np.arange(0, T, 1, dtype=np.float64)
	time = np.arange(0, T, 1, dtype=np.float64)
	for i in range(T):
		[x, y] = p.next_step(1)
		value[i] = y

	plt.plot(time, value)
	plt.show()

class System:
	def __init__(self, p, r, ):
		self.p = p
		self.r = r

def test_controll(p, r):
	T = 1000
	UC = 25
	value = np.arange(0, T, 1, dtype=np.float64)
	time = np.arange(0, T, 1, dtype=np.float64)
	for i in range(1, T):
		e = UC-value[i-1]
		u = r.next_step(e)
		[x, y] = p.next_step(u)
		value[i] = y

	plt.plot(time, value)
	plt.show()

# p = Process()
# test_process(p)
# r = Controller(0.7, 0.5, 0.2)
# test_controll(p, r)


