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

# Зеленые точки
points_g = [] 
points_data_g = [] 
speeds_g = []

for i in range(k):
    x_g = random.uniform(-5, 5)
    y_g = random.uniform(-5, 5)
    speed = random.uniform(0.5, 1.5)
    points_data_g.append([x_g, y_g])
    
    angle_g = random.uniform(0, 2*np.pi)
    vx_g = speed * np.cos(angle_g)
    vy_g = speed * np.sin(angle_g)
    speeds_g.append([vx_g, vy_g])
    
    point, = ax.plot([x_g], [y_g], 'o', color='green', markersize=5)
    points_g.append(point)

# Синие точки
points_b = [] 
points_data_b = [] 
speeds_b = []

for i in range(k):
    x_b = random.uniform(-5, 5)
    y_b = random.uniform(-5, 5)
    speed = random.uniform(0.5, 1.5)
    points_data_b.append([x_b, y_b])
    
    angle_b = random.uniform(0, 2*np.pi)
    vx_b = speed * np.cos(angle_b)
    vy_b = speed * np.sin(angle_b)
    speeds_b.append([vx_b, vy_b])
    
    point, = ax.plot([x_b], [y_b], 'o', color='blue', markersize=5)
    points_b.append(point)

# Красная точка (вирус)
points_r = [] 
points_data_r = [] 
speeds_r = []

for i in range(1):
    x_r = random.uniform(-5, 5)
    y_r = random.uniform(-5, 5)
    speed = random.uniform(0.5, 1.5)
    points_data_r.append([x_r, y_r])
    
    angle_r = random.uniform(0, 2*np.pi)
    vx_r = speed * np.cos(angle_r)
    vy_r = speed * np.sin(angle_r)
    speeds_r.append([vx_r, vy_r])
    
    point, = ax.plot([x_r], [y_r], 'o', color='red', markersize=7)
    points_r.append(point)

# Единая функция обновления
def update(frame):
    # Обновление зеленых точек
    for i, point in enumerate(points_g):
        x_g, y_g = points_data_g[i]
        vx_g, vy_g = speeds_g[i]
        
        x_new = x_g + vx_g * 0.1  
        y_new = y_g + vy_g * 0.1
        
        if abs(x_new) >= 5:
            vx_g = -vx_g
            speeds_g[i][0] = vx_g
            x_new = x_g + vx_g * 0.1
            
        if abs(y_new) >= 5:
            vy_g = -vy_g
            speeds_g[i][1] = vy_g
            y_new = y_g + vy_g * 0.1
        
        points_data_g[i] = [x_new, y_new]
        point.set_data([x_new], [y_new])
    
    # Обновление синих точек
    for i, point in enumerate(points_b):
        x_b, y_b = points_data_b[i]
        vx_b, vy_b = speeds_b[i]
        
        x_new = x_b + vx_b * 0.1
        y_new = y_b + vy_b * 0.1
        
        if abs(x_new) >= 5:
            vx_b = -vx_b
            speeds_b[i][0] = vx_b
            x_new = x_b + vx_b * 0.1
            
        if abs(y_new) >= 5:
            vy_b = -vy_b
            speeds_b[i][1] = vy_b
            y_new = y_b + vy_b * 0.1
        
        points_data_b[i] = [x_new, y_new]
        point.set_data([x_new], [y_new])
    
    # Обновление красной точки
    if points_r: 
        point = points_r[0]
        x_r, y_r = points_data_r[0]
        vx_r, vy_r = speeds_r[0]
        
        x_new = x_r + vx_r * 0.1
        y_new = y_r + vy_r * 0.1
        
        if abs(x_new) >= 5:
            vx_r = -vx_r
            speeds_r[0][0] = vx_r
            x_new = x_r + vx_r * 0.1
            
        if abs(y_new) >= 5:
            vy_r = -vy_r
            speeds_r[0][1] = vy_r
            y_new = y_r + vy_r * 0.1
        
        points_data_r[0] = [x_new, y_new]
        point.set_data([x_new], [y_new])
    
    # Возвращаем все обновленные точки
    return points_g + points_b + points_r

# Исправленный вызов FuncAnimation
anim = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)
anim.save('virus_2.gif')
plt.show()