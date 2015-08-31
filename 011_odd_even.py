from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


im = Image.open('cave.jpg')
print(im.format, im.size, im.mode)
#print(im.getpixel((1,1)))
r = np.zeros((im.size[0]/2, im.size[1]))
g = np.zeros((im.size[0]/2, im.size[1]))
b = np.zeros((im.size[0]/2, im.size[1]))

for j in range(0,im.size[1],1):
    for i in range(0,im.size[0],1):
        if (i + j) % 2 == 0:
            r[i/2][j] = (im.getpixel((i,j))[0])
            g[i/2][j] = (im.getpixel((i,j))[1])
            b[i/2][j] = (im.getpixel((i,j))[2])

#print r[:100]
#print g[:100]
print b.shape
data = r+g+b

fig, ax = plt.subplots()
heatmap = ax.pcolor(data, cmap=plt.cm.Blues)
plt.show()

#solution = 'evil'
