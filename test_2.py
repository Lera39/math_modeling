import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.animation import FuncAnimation

class Person:
    def __init__(self, x, y, speed_x, speed_y, contacts, kof_ver, time_i, time_r, chance = False, is_infected = False):   
        self.x = x
        self.y = y
        self.speed_x = speed_x * np.cos(angel)
        self.speed_y = speed_y * np.sin(angel)
        self.chance = chance
        self.is_infected = is_infected
        self.time_i = time_i
        self.time_r = time_r
        self.contacts = contacts
        self.kof_ver = kof_ver
        

    def update(self):
        self.x = self.x + self.speed_x * 0.1
        self.y = self.y + self.speed_y * 0.1
        if abs(self.x) >= 5:
            self.speed_x = -self.speed_x
            
        if abs(self.y) >= 5:
            self.speed_y = -self.speed_y


    def near_infect(self, persons):
        if self.kof_ver >= 0.5:
            for person in persons:
                if (person != self and self.chance != True and person.is_infected
                and (((person.x - self.x) ** 2 + (person.y - self.y) ** 2) < 0.1)):
                    return True
        return False


    def infect(self):
            self.is_infected = True


    def change_contacts(self, persons):
        for person in persons:
            if (person != self and person.is_infected == True and (((person.x - self.x) ** 2 + (person.y - self.y) ** 2) < 0.1)):
                self.kof_ver += 0.00005
                self.contacts += 1
        return self.kof_ver, self.contacts


    def lost_i(self):
        if self.is_infected == True and self.time_i >= 1:
            self.is_infected = False
            self.time_i = 0
            self.chance = True

    def lost_r(self):
        if self.chance == True and self.time_r >=1:
            self.chance = False
            self.time_r = 0


figure, axises = plt.subplots()

persons = []
k = random.randint(80, 120)

for i in range (k):
    angel = random.random() * 2 * np.pi
    time_i = 0
    time_r = 0
    contacts = 0

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
        contacts,
        random.uniform(0.4, 0.6),   #kof_ver
        time_i,
        time_r,
        chance,
        is_infected,
    ))

figure, axises = plt.subplots()
 
animation_red_points, = plt.plot([], [], 'o', color = 'red')
animation_green_points, = plt.plot([], [], 'o', color = 'green')
animation_blue_points, = plt.plot([], [], 'o', color = 'blue')

# title_obj = axises.set_title(f'S = {S}, I = {I}, R = {R}, time = 0')

def update(frame):
    data_red_points_x = []
    data_red_points_y = []
    data_green_points_x = []
    data_green_points_y = []
    data_blue_points_x = []
    data_blue_points_y = []

    # S = len(data_green_points_x)
    # I = len(data_red_points_x)
    # R = len(data_blue_points_x)
    # title_obj.set_text(f'S = {S}, I = {I}, R = {R}, time = {0.1*frame}')

    for person in persons:
        person.update()

        if person.is_infected == True:
            person.time_i += 0.002
            person.lost_i()
        elif person.chance == True:
            person.time_r += 0.0002
            person.lost_r()

        person.change_contacts(persons)
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

    # β = (len(data_green_points_x) / time) * k / len(data_red_points_x) / len(data_green_points_x) * (-1)   # коэффициент заражения
    # γ = len(data_blue_points_x) / (time * len(data_red_points_x))   # коэффициент выздоровления

    return animation_red_points, animation_green_points, animation_blue_points


axises.set_xlim(-5, 5)
axises.set_ylim(-5, 5)
frames = np.arange(400)
animation = FuncAnimation(figure, update, frames=frames, interval=50)
animation.save('virus.gif')
plt.show()