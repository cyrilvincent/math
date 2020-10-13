from PIL import Image
import numpy as np

im1 = Image.open("data/ski.jpg")
a1 = np.asarray(im1)
print(a1.shape)

im2 = Image.open("data/ski2.jpg")
a2 = np.asarray(im2)
print(a2.shape)

xmin = min(a1.shape[0], a2.shape[0])
print(xmin)
ymin = min(a1.shape[1], a2.shape[1])
print(ymin)

red1 = a1[:xmin, :ymin, 0]
avg2 = np.mean(a2[:xmin, :ymin], axis=2)
print(red1.shape)
print(avg2.shape)
res = (red1 + avg2) / 2

im = Image.fromarray(res).convert('RGB')
im.save("data/addition.png")

# cube1 =  a1[:xmin, :ymin]
# red2 = a2[:xmin, :ymin, 0]
# cube1[:,:,1] = red2
# im = Image.fromarray(cube1)
# im.save("data/additionrvb.png")