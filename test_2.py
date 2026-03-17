import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.animation import FuncAnimation

class Person:
    def __init__(self, x, y, speed_x, speed_y, chance = False, is_infected = False):    # + period
        self.x = x
        self.y = y
        self.speed_x = speed_x * np.cos(angel)
        self.speed_y = speed_y * np.sin(angel)
        self.chance = chance
        self.is_infected = is_infected
        #self.period = period
        
    def update(self):
        self.x = self.x + self.speed_x * 0.1
        self.y = self.y + self.speed_y * 0.1
        if abs(self.x) >= 5:
            # self.x = -self.x
            self.speed_x = -self.speed_x
            # self.x = self.x + self.speed_x * 0.1
            
        if abs(self.y) >= 5:
            # self.y = -self.y
            self.speed_y = -self.speed_y
            # self.y = self.y + self.speed_y * 0.1

    def near_infect(self, persons):
        for person in persons:
            if person != self and self.chance != True and person.is_infected and (((person.x - self.x) ** 2 + (person.y - self.y) ** 2) < 0.1):
                return True
        return False

    def infect(self):
        self.is_infected = True

figure, axises = plt.subplots()

persons = []
k = random.randint(80, 120)

for i in range (k):

    angel = random.random() * 2 * np.pi

    v = random.random()
    immun = random.randint(1,15)
    if v < 0.07:
        chance = False
        is_infected = True
    elif v >= 0.07:
        if immun > 14:
            chance = True
            is_infected = False
        else:
            chance = False
            is_infected = False

    persons.append(Person(
        random.uniform(-5, 5),    # x
        random.uniform(-5, 5),    # y
        random.uniform(0.2, 0.4),   #speed_x
        random.uniform(0.2, 0.4),   #speed_y
        chance,
        is_infected,
        #random.uniform(0.25, 0.5)   #period
    ))

figure, axises = plt.subplots()
 
animation_red_points, = plt.plot([], [], 'o', color='red')
animation_green_points, = plt.plot([], [], 'o', color='green')
animation_blue_points, = plt.plot([], [], 'o', color='blue')

def update(frame):
    data_red_points_x = []
    data_red_points_y = []
    data_green_points_x = []
    data_green_points_y = []
    data_blue_points_x = []
    data_blue_points_y = []
 
    for person in persons:
        person.update()
 
        if person.near_infect(persons):
            person.infect()
 
        if person.is_infected:
            data_red_points_x.append(person.x)
            data_red_points_y.append(person.y)
        elif person.chance:
            data_blue_points_x.append(person.x)
            data_blue_points_y.append(person.y)
        else:
            data_green_points_x.append(person.x)
            data_green_points_y.append(person.y)

  
    animation_red_points.set_data(data_red_points_x, data_red_points_y)
    animation_green_points.set_data(data_green_points_x, data_green_points_y)
    animation_blue_points.set_data(data_blue_points_x, data_blue_points_y)
    return animation_red_points, animation_green_points, animation_blue_points

axises.set_xlim(-5, 5)
axises.set_ylim(-5, 5)
frames = np.arange(200)


animation = FuncAnimation(figure, update, frames=frames, interval=50)
animation.save('virus.gif')
plt.show()