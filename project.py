import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-15, 15)  
ax.set_ylim(-15, 15) 
ax.grid(True, alpha=0.3)

speeds = []
points = []
k = random.randint(10, 25)
frames = 200

# Создаем зеленые точки
for i in range(k):
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    point, = ax.plot([x], [y], 'o', color='green') 
    speed = random.uniform(0.5, 1.5)
    speeds.append(speed)
    points.append(point)

# Создаем красную точку (вирус)
x_virus = random.uniform(-5, 5) 
y_virus = random.uniform(-5, 5)
virus, = ax.plot([x_virus], [y_virus], 'o', color='red')

def position(frame, speed):
    t = frame / frames * 4 * np.pi
    x = speed * t
    y = speed * t
    return x, y

def init():
    for point in points:
        point.set_data([x_virus], [y_virus]) 
    virus.set_data([x_virus], [y_virus])
    return points + [virus]

def update(frame):
    # Обновляем позиции зеленых точек
    for i, point in enumerate(points):
        a=random.uniform(-2,2)
        speed = speeds[i]
        x_new = x_virus + speed * frame + a
        y_new = y_virus + speed * frame + a
        point.set_data([x_new], [y_new])
    
    # Обновляем позицию вируса
    a = random.uniform(-2,2)
    x_new = x_virus + 0.5 * frame + a
    y_new = y_virus + 0.5 * frame + a
    virus.set_data([x_new], [y_new])
    
    return points + [virus]

anim = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)
anim.save('virus.gif')
plt.show()