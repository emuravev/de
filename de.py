import numpy as np
import matplotlib.pyplot as plt
import math

""""Initial part*****************************************************************************************************"""

fig = plt.figure()

ax1_1 = fig.add_subplot(7, 2, 1)
plt.grid(True)
ax1_1.set_title("Euler")
ax2_1 = fig.add_subplot(7, 2, 2)
plt.grid(True)
ax2_1.set_title("Error for Euler")

ax1_2 = fig.add_subplot(7, 2, 5)
plt.grid(True)
ax1_2.set_title("Improved Euler")
ax2_2 = fig.add_subplot(7, 2, 6)
plt.grid(True)
ax2_2.set_title("Error for Improved Euler")

ax1_3 = fig.add_subplot(7, 2, 9)
plt.grid(True)
ax1_3.set_title("Runge Kutta")
ax2_3 = fig.add_subplot(7, 2, 10)
plt.grid(True)
ax2_3.set_title("Error for Runge Kutta")

ax3_1 = fig.add_subplot(7, 2, 13)
plt.grid(True)
ax3_1.set_title("Solution")
ax3_2 = fig.add_subplot(7, 2, 14)
plt.grid(True)
ax3_2.set_title("Error for solution")

print("Enter initial conditions")
x0 = int(input("\tx0: "))
y0 = int(input("\ty0: "))
X = float(input("\tX:  "))
steps = int(input("Enter number of steps: "))
С = ((math.sin(x0) + 1) + y0)/math.exp(math.sin(x0))

h = (X - x0) / (steps - 1)
x = np.linspace(x0, X + h, steps)

""""Part of Euler method*********************************************************************************************"""

y = np.zeros(steps)
y[0] = y0

for i in range(1, steps):
    y[i] = y[i - 1] + h * (0.5 * math.sin(2 * x[i - 1]) + y[i - 1] * math.cos(x[i]))

ax1_1.plot(x, y, "navy", label="Euler")
ax2_1.plot(x, list(map(lambda a, b: (b - (С * math.exp(math.sin(a)) - math.sin(a) - 1)), x, y)), "darkred",
           label="Error for Euler")

""""Part of Improved Euler method************************************************************************************"""

y = np.zeros(steps)
y[0] = y0

for i in range(1, steps):
    x_cur = x[i - 1] + h / 2
    y_cur = y[i - 1] + (h / 2) * (0.5 * math.sin(2 * x[i - 1]) + y[i - 1] * math.cos(x[i]))
    y[i] = y[i - 1] + h * (0.5 * math.sin(2 * x_cur) + y_cur * math.cos(x_cur))

ax1_2.plot(x, y, "blue", label="Improved Euler")
ax2_2.plot(x, list(map(lambda a, b: (b - (С * math.exp(math.sin(a)) - math.sin(a) - 1)), x, y)), "firebrick",
           label="Error for Improved Euler")

""""Part of Runge Kutta method***************************************************************************************"""

y = np.zeros(steps)
y[0] = y0

for i in range(1, steps):
    k1 = 0.5 * math.sin(2 * x[i - 1]) + y[i - 1] * math.cos(x[i - 1])
    k2 = 0.5 * math.sin(2 * (x[i - 1] + h / 2)) + (y[i - 1] + h * k1 / 2) * math.cos(x[i - 1] + h / 2)
    k3 = 0.5 * math.sin(2 * (x[i - 1] + h / 2)) + (y[i - 1] + h * k2 / 2) * math.cos(x[i - 1] + h / 2)
    k4 = 0.5 * math.sin(2 * (x[i - 1] + h)) + (y[i - 1] + h * k3) * math.cos(x[i - 1] + h)
    y[i] = y[i - 1] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

ax1_3.plot(x, y, "green", label="Runge Kutta")
ax2_3.plot(x, list(map(lambda a, b: (b - (С * math.exp(math.sin(a)) - math.sin(a) - 1)), x, y)), "red",
           label="Error for Runge Kutta")

""""Part of solution*************************************************************************************************"""

ax3_1.plot(x, list(map(lambda a: С * math.exp(math.sin(a)) - math.sin(a) - 1, x)), "black", label="Solution")
ax3_2.plot(x, list(map(lambda a: (С * math.exp(math.sin(a)) - math.sin(a) - 1 - (С * math.exp(math.sin(a)) - math.sin(a) - 1)), x)), "black", label="Error for solution")

""""Output part******************************************************************************************************"""

print("Initial conditions")
print("\tx0: " + str(x0))
print("\ty0: " + str(y0))
print("\tX:  " + str(X))
print("Number of steps: " + str(steps))
plt.show()
