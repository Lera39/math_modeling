import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-15,15)
ax.set_ylim(-15,15)
ax.grid(True, alpha=0.3)

speeds = []
points = []
k = random.randint(10,25)
frames = 200

for i in range (k):
    x = random.uniform(-15,15)
    y = random.uniform(-15,15)
    point = ax.plot([x],[y], 'o', color = 'green')
    speed = random.uniform(0.5,1.5)
    speeds.append(speed)
    points.append(point)

x = random.uniform(-15,15)
y = random.uniform(-15,15)
virus, = ax.plot([x],[y], 'o', color = 'red')

def position(frame):
    t = frame/frames * 4 * np.pi
    x = speed * t
    y = speed * t
    return x,y

def init():
    point.set_data([x],[y])
    return point

def update(frame):
    point.set_data([x],[y])
    return point

anim = FuncAnimation(fig, update, frames = frames)
plt.savefig('123.gif')
plt.show()