import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 30)
y = x**2
plt.plot(x, y)
plt.show()

x = np.linspace(-3, 3, 30)
y = x ** 2
plt.plot(x, y, 'r.')
plt.show()

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x), 'r-')
plt.plot(x, -np.sin(x), 'g--')
plt.show()