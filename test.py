import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)  
ax.set_ylim(-5, 5) 
ax.grid(True, alpha=0.3)

k = random.randint(10, 25)
frames = 400

# списки для хранения данных зеленых точек
points_g = [] 
points_data_g = [] 
speeds_g = []
# зеленые точки
for i in range(k):
    x_g = random.uniform(-5, 5)
    y_g = random.uniform(-5, 5)
    speed = random.uniform(0.5, 1.5)
    points_data_g.append([x_g, y_g])
    
    angle_g = random.uniform(0, 2*np.pi)
    vx_g = speed * np.cos(angle_g)
    vy_g = speed * np.sin(angle_g)
    speeds_g.append([vx_g, vy_g])
    
    # объект точки
    point, = ax.plot([x_g], [y_g], 'o', color='green', markersize=5)
    points_g.append(point)

# списки для хранения данных синих точек
points_b = [] 
points_data_b = [] 
speeds_b = []
# синие точки
for i in range(k):
    x_b = random.uniform(-5, 5)
    y_b = random.uniform(-5, 5)
    speed = random.uniform(0.5, 1.5)
    points_data_b.append([x_b, y_b])
    
    angle_b = random.uniform(0, 2*np.pi)
    vx_b = speed * np.cos(angle_b)
    vy_b = speed * np.sin(angle_b)
    speeds_b.append([vx_b, vy_b])
    
    # объект точки
    point, = ax.plot([x_b], [y_b], 'o', color='blue', markersize=5)
    points_b.append(point)

# списки для хранения данных красных точек
points_r = [] 
points_data_r = [] 
speeds_r = []
# зеленые точки
for i in range(k):
    x_r = random.uniform(-5, 5)
    y_r = random.uniform(-5, 5)
    speed = random.uniform(0.5, 1.5)
    points_data_r.append([x_g, y_g])
    
    angle_r = random.uniform(0, 2*np.pi)
    vx_r = speed * np.cos(angle_r)
    vy_r = speed * np.sin(angle_r)
    speeds_r.append([vx_r, vy_r])
    
    # объект точки
    point, = ax.plot([x_r], [y_r], 'o', color='red', markersize=5)
    points_r.append(point)

def update(frame):
    global x_virus, y_virus, vx_virus, vy_virus
    
    # Обновляем позиции зеленых точек
    for i, point in enumerate(points_g):
        x_g, y_g = points_data_g[i]
        vx_g, vy_g = speeds_g[i]
        
        # Обновляем координаты
        x_new = x_g + vx_g * 0.1  
        y_new = y_g + vy_g * 0.1
        
        # Отражение от границ
        if abs(x_new) >= 5:
            vx_g = -vx_g
            speeds_g[i][0] = vx_g
            x_new = x_g + vx_g * 0.1
            
        if abs(y_new) >= 5:
            vy_g = -vy_g
            speeds_g[i][1] = vy_g
            y_new = y_g + vy_g * 0.1
        
        # Сохраняем новые координаты
        points_data_g[i] = [x_new, y_new]
        point.set_data([x_new], [y_new])
    
    # Обновляем позицию вируса
    x_virus = x_virus + vx_virus * 0.1
    y_virus = y_virus + vy_virus * 0.1
    
    # Отражение вируса от границ
    if abs(x_virus) >= 5:
        vx_virus = -vx_virus
        x_virus = x_virus + vx_virus * 0.1  # корректируем позицию после отражения
        
    if abs(y_virus) >= 5:
        vy_virus = -vy_virus
        y_virus = y_virus + vy_virus * 0.1  # корректируем позицию после отражения
    
    # Обновляем позицию вируса на графике
    virus.set_data([x_virus], [y_virus])
    
    return points_g + [virus]

anim = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)
anim.save('virus_2.gif')
plt.show()