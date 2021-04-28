import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('matplotlib_image.jpg')
plt.imsave("logo.png", img, cmap = 'gray', origin = 'lower')
plt.imshow(img)
plt.show()