#for better understading the example, go to https://en.wikipedia.org/wiki/Harmonic_oscillator#Spring–mass_system, 
#in the damped harmonic oscillator section.

import matplotlib.pyplot as plt
from rk_solver import RK4

# Coefficient of Friction
R = .1

# Spring Constant
D = 1

# Mass
m = 0.1

ydot = lambda t, x, y: -(R*y + D*x) / m
xdot = lambda t, x, y: -(m*ydot(t, x, y) + D*x) / R

lv = RK4(xdot, ydot)
t, y = lv.solve([0, 1], .01, 20)

plt.plot(t, y[0], label = 'Velocity')
plt.plot(t, y[1], label = 'Displacement')
plt.legend()
plt.show()
