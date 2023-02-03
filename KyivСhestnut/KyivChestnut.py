import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits import mplot3d

fig = plt.figure(facecolor = 'black')
ax = plt.axes(projection = '3d')
plt.axis('off')
ax.set_facecolor('#000000')

# Barnsley FERN from wiki:
x = [0]
y = [0]

for i in range(0, 2000):
    z = random.randint(1, 100)
    if z == 1:
        x.append(0)
        y.append(0.16 * y[i])
    if z >= 2 and z <= 86:
        x.append(0.85 * x[i] + 0.04 * y[i])
        y.append(-0.04 * x[i] + 0.85 * y[i] + 1.6)
    if z >= 87 and z <= 93:
        x.append(0.2 * x[i] - 0.26 * y[i])
        y.append(0.23 * x[i] + 0.22 * y[i] + 1.6)
    if z >= 94 and z <= 100:
        x.append(-0.15 * x[i] + 0.28 * y[i])
        y.append(0.26 * x[i] + 0.24 * y[i] + 0.44)

# FLOWER ADD from wiki:
theta = np.linspace(0, 2 * np.pi, 1000)
r = 3 * np.sin(4 * theta)                                                       # it was 3 and 6 before
x1 = r * np.cos(theta)
y1 = r * np.sin(theta)


# GREEN FERN VISUALISATION in PLOT:
ax.scatter(x, y, color = '#ccccff', zorder = 1)                                 # #80ffbf

# IRIS FLOWER VISUALISATION:
ax.plot(x1, y1, color = '#80ffbf', marker = 'o', markersize = 4, zorder = 1)    # #CCCCFF  #8080ff markersize =thiknes

ax.view_init(elev = 30, azim = 5)
plt.show()