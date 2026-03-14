import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)  
ax.set_ylim(-5, 5) 
ax.grid(True, alpha=0.3)

k = random.randint(10, 25)
frames = 200

points = [] 
points_data = [] 
speeds = []

# зеленые точки
for i in range(k):
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    speed = random.uniform(0.5, 1.5)
    points_data.append([x, y])

     # объект точки
    point, = ax.plot([x], [y], 'o', color='green', markersize=5)
    points.append(point)

x_virus = random.uniform(-5, 5) 
y_virus = random.uniform(-5, 5)
virus, = ax.plot([x_virus], [y_virus], 'o', color='red', markersize=8)

plt.savefig('pr.png')
plt.show()