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

# списки для хранения данных зеленых точек
points = [] 
points_data = [] 
speeds = []

# зеленые точки
for i in range(k):
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    speed = random.uniform(0.5, 1.5)
    points_data.append([x, y])
    
    angle = random.uniform(0, 2*np.pi)
    vx = speed * np.cos(angle)
    vy = speed * np.sin(angle)
    speeds.append([vx, vy])
    
    # объект точки
    point, = ax.plot([x], [y], 'o', color='green', markersize=5)
    points.append(point)

# Создаем красную точку (вирус)
x_virus = random.uniform(-5, 5) 
y_virus = random.uniform(-5, 5)
virus, = ax.plot([x_virus], [y_virus], 'o', color='red', markersize=8)

# Задаем скорость вируса отдельно
virus_speed = random.uniform(0.5, 1.5)
angle_virus = random.uniform(0, 2*np.pi)
vx_virus = virus_speed * np.cos(angle_virus)
vy_virus = virus_speed * np.sin(angle_virus)

def update(frame):
    global x_virus, y_virus, vx_virus, vy_virus
    
    # Обновляем позиции зеленых точек
    for i, point in enumerate(points):
        x, y = points_data[i]
        vx, vy = speeds[i]
        
        # Обновляем координаты
        x_new = x + vx * 0.1  
        y_new = y + vy * 0.1
        
        # Отражение от границ
        if abs(x_new) >= 5:
            vx = -vx
            speeds[i][0] = vx
            x_new = x + vx * 0.1
            
        if abs(y_new) >= 5:
            vy = -vy
            speeds[i][1] = vy
            y_new = y + vy * 0.1
        
        # Сохраняем новые координаты
        points_data[i] = [x_new, y_new]
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
    
    return points + [virus]

anim = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)
anim.save('virus_2.gif')
plt.show()