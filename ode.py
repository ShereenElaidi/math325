# a code to learn how to solve ODEs in Python

import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 

# a function that returns dy/dt

def model(y, t): 
	k = 0.3
	dydt = -k*y 
	return dydt 

# setting the initial conditin 
y0 = 5

# time points
t = np.linspace(0,20)

# solving the ODE
y = odeint(model, y0, t)

# plotting the results
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show() 


# Exercises. 
# Problem 1 

def model1(y,t):
	k = -1 
	dydt = k*y + 1 
	return dydt 

# setting initial condition
y0 = 0 

# time points
t = np.linspace(0, 20)

# solving the ODE
y = odeint(model1, y0, t)

# plotting the results
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show() 
