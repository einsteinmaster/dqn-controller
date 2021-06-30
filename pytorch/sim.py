import numpy as np
import matplotlib.pyplot as plt

T_MAX = 5000

DELAY = T_MAX // 5

class Sim():
	def __init__(self) -> None:
		self.reset()

	def step(self,action):
		action = action / DELAY
		#print(action)

		self.hist_control[self.t] = action

		if(self.t > 0):
			self.hist_integral[self.t] = self.hist_integral[self.t - 1] + action
		else:
			self.hist_integral[self.t] = 0

		if(self.t - DELAY >= 0):
			self.state[0] = self.hist_integral[self.t - DELAY]
			self.state[1] = self.hist_control[self.t - DELAY]
			self.state[2] = self.t / T_MAX

		dev = (self.t / 5000) - self.hist_integral[self.t]

		self.error += dev * dev

		self.t = self.t + 1

		if(self.t >= T_MAX):
			return self.state, -np.log(self.error + 0.00001) , True
		else:
			return self.state, -np.log(self.error + 0.00001) , False

	def reset(self):
		self.t = 0
		self.hist_control = np.zeros(T_MAX)
		self.hist_integral = np.zeros(T_MAX)
		self.state = np.zeros(3)
		self.error = 0
		return self.state

	def render(self):
		pass

	def close(self):
		plt.plot([t/5000 for t in range(5000)],label="set")
		plt.plot(self.hist_integral,label="is")
		plt.show()
		pass