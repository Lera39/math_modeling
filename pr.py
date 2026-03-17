import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

class Person:
    def init(self, x, y, speed_x, speed_y, chance=False, is_infected=False):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.chance = chance
        self.is_infected = is_infected

    def near_infect(self, persons):
        for person in persons:
            if (person != self and 
                not self.chance and 
                person.is_infected and 
                ((person.x - self.x)**2 + (person.y - self.y)**2) < 0.1):
                return True
        return False

    def infect(self):
        self.is_infected = True

    def update(self):
        self.x += self.speed_x * 0.1
        self.y += self.speed_y * 0.1

# Создаем figure один раз
figure, axises = plt.subplots()
animation_red_points, = plt.plot([], [], 'o', color='red')
animation_green_points, = plt.plot([], [], 'o', color='green')

# Создаем экземпляры классов правильно
persons = [
    Person(1, 1, 0.1, 0.1, False, True),   # Зараженный
    Person(1, 2, 0.05, 0.05, False, False)  # Здоровый
]

def update(frame):
    data_red_points_x = []
    data_red_points_y = []
    data_green_points_x = []
    data_green_points_y = []
    
    for person in persons:
        person.update()
        
        if person.near_infect(persons):
            person.infect()
        
        if person.is_infected:
            data_red_points_x.append(person.x)
            data_red_points_y.append(person.y)
        else:
            data_green_points_x.append(person.x)
            data_green_points_y.append(person.y)
    
    animation_red_points.set_data(data_red_points_x, data_red_points_y)
    animation_green_points.set_data(data_green_points_x, data_green_points_y)
    return animation_red_points, animation_green_points

axises.set_xlim(0, 5)
axises.set_ylim(0, 5)
frames = np.arange(100)

animation = FuncAnimation(figure, update, frames=frames, interval=50, blit=True)
animation.save('pr.gif', writer='pillow')
plt.show()