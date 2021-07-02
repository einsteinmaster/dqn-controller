import numpy as np
import matplotlib.pyplot as plt

T_MAX = 50

DELAY = T_MAX // 5

ALPHA = 4.0 / T_MAX

class Sim():
	def __init__(self) -> None:
		self.T_MAX = T_MAX
		self.DELAY = DELAY
		self.reset()

	def step(self,action):
		action = action / DELAY
		if self.t > 0:
			action = ALPHA * action + (1-ALPHA) * self.hist_control[self.t-1]
		else:
			action = 0
		#print(action)

		self.hist_control[self.t] = action

		if(self.t > 0):
			self.hist_integral[self.t] = self.hist_integral[self.t - 1] + action
		else:
			self.hist_integral[self.t] = 0

		if(self.t - DELAY >= 0):
			self.state[0] = self.t / T_MAX
			self.state[1] = self.hist_integral[self.t - DELAY]
			#self.state[2] = self.hist_control[self.t - DELAY]
			
		dev = (self.t / T_MAX) - self.hist_integral[self.t]

		self.error += dev * dev

		self.t = self.t + 1

		if(self.t >= T_MAX):
			#ret_err = -np.log(self.error + 0.00000000001) + 10
			ret_err = -self.error
			return self.state, ret_err , True
		else:
			return self.state, 0 , False

	def reset(self):
		self.t = 0
		self.hist_control = np.zeros(T_MAX)
		self.hist_integral = np.zeros(T_MAX)
		self.state = np.zeros(2)
		self.error = 0
		return self.state

	def render(self):
		pass

	def close(self):
		fig, axs = plt.subplots(2)
		axs[0].plot([t/T_MAX for t in range(T_MAX)],label="set")
		axs[0].plot(self.hist_integral,label="is")
		axs[1].plot(self.hist_control,label="control")
		axs[0].legend()
		axs[1].legend()
		plt.show()
		pass