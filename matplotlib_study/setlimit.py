import matplotlib.pyplot as plt
fig = plt.figure()
a1 = fig.add_axes([0,0,1,1])
import numpy as np
x = np.arange(1,10)
a1.plot(x, np.exp(x))
a1.set_title('exp')
plt.show()

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,4))
a1 = fig.add_axes([0.1,0.1,1,1])
import numpy as np
x = np.arange(1,10)
a1.plot(x, np.exp(x),'r')
a1.set_title('exp')
a1.set_ylim(0,10000)
a1.set_xlim(0,10)
plt.show()

