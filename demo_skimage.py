from skimage import io
import matplotlib.pyplot as plt
import numpy as np
im = io.imread('d:/T23S0746.8_CC28-2825A_SD_EPI_SIP_API_11_11.tif')
print(im.shape)
res = im[:90:3,:,:]
print(res.shape)
plt.imshow(res[0], cmap='Greys')
plt.show()
fig, axs = plt.subplots(nrows=6, ncols=5)
i=0
for ax in axs.reshape(-1):
    ax.imshow(res[i], cmap='Greys')
    i+=1
plt.show()

diff = np.abs(res[0] - res[1])
print(res[0])
print(res[1])
print(diff)
plt.imshow(diff)
plt.show()

