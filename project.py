import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)  
ax.set_ylim(-5, 5) 
ax.grid(True, alpha=0.3)

speeds = []
points = []
k = random.randint(10, 25)
frames = 200

# Создаем зеленые точки
for i in range(k):
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    speed = random.uniform(0.05, 0.5)
    points.append([x, y])

    angle = random.uniform(0.2, 2*np.pi)
    vx = speed * np.cos(angle)
    vy = speed * np.sin(angle)
    speeds.append([vx, vy])

# Создаем красную точку (вирус)
x_virus = random.uniform(-5, 5) 
y_virus = random.uniform(-5, 5)
virus, = ax.plot([x_virus], [y_virus], 'o', color='red')
virus_pos = [x_virus, y_virus]
virus_speed = [random.uniform(0.05,0.5), random.uniform(0.05,0.5)]

def position(frame, speed):
    t = frame / frames * 4 * np.pi
    x = speed * t
    y = speed * t
    return x, y

def init():
    # for point in points:
        # point.set_data([x_virus], [y_virus]) 
    virus.set_data([x_virus], [y_virus])
    return points + [virus]

def update(frame):
    # Обновляем позиции зеленых точек
    for i, point in enumerate(points):
        x, y = points[i]
        vx, vy = speeds[i]
        x_new = x_virus + vx
        y_new = y_virus + vy
        if x_new >= 5:
            x_new = 5 - (x_new - 5)
            speeds[i][0] = -vx
        elif x_new <= -5:
            x_new = -5 + (5 - x_new)
            speeds[i][0] = -vx

        if y_new >= 5:
            y_new = 5 - (y_new - 5)
            speeds[i][1] = -vy
        elif y_new <= -5:
            y_new = -5 + (-5 - y_new)
            speeds[i][1] = -vy
            
        points[i] = [x_new, y_new]
        # point.set_data([x_new], [y_new])
    
    # Обновляем позицию вируса
    vx, vy = virus_speed
    x_new = virus_pos[0] + vx
    y_new = virus_pos[0] + vy
    if x_new >= 5:
        x_new = 5 - (x_new - 5)
        speeds[i][0] = -vx
    elif x_new <= -5:
        x_new = -5 + (5 - x_new)
        speeds[i][0] = -vx

    if y_new >= 5:
        y_new = 5 - (y_new - 5)
        speeds[i][1] = -vy
    if y_new <= -5:
        y_new = -5 + (-5 - y_new)
        speeds[i][1] = -vy

    virus_pos[0] = x_new
    virus_pos[1] = y_new
    virus.set_data([x_new], [y_new])
    return points + [virus]

anim = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)
anim.save('virus.gif')
plt.show()