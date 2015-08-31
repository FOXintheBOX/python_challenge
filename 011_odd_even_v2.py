from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


im = Image.open('cave.jpg')
print(im.format, im.size, im.mode)
#print(im.getpixel((1,1)))
pixel = np.zeros((im.size[0]/2, im.size[1], 3))

for j in range(0,im.size[1],1):
    for i in range(0,im.size[0],1):
        if (i + j) % 2 == 0:
            pixel[i/2][j] = im.getpixel((i,j))

data = pixel.sum(axis = 2)

fig, ax = plt.subplots()
heatmap = ax.pcolor(data, cmap=plt.cm.Blues)
plt.show()

#solution = 'evil'
