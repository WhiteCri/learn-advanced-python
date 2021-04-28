import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) # left, bottom, width, height

ax.set_title('sine wave')
ax.set_xlabel('angle')
ax.set_ylabel('sine')

ax.plot(x, y)
plt.show()