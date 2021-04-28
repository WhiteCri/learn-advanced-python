import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(10,4))
x = np.arange(1,5)
axes[0].plot(x, np.exp(x))
axes[0].plot(x, x**2)
axes[0].set_title("Normal scale")
axes[1].plot(x, np.exp(x))
axes[1].plot(x, x**2)
axes[1].set_yscale("log") ####
axes[1].set_title("Logarithmic scale (y)")
axes[0].set_xlabel("x axis")
axes[0].set_ylabel("y axis")
axes[0].xaxis.labelpad = 10
axes[1].set_xlabel("x axis")
axes[1].set_ylabel("y axis")
plt.show()

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 1, 1])
ax.spines['bottom'].set_color('blue')
ax.spines['left'].set_color('red')
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_color(None)
ax.spines['top'].set_color(None)
ax.plot([1,2,3,4,5])
plt.show()