import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.plot([10,10,0],[0,10,10], color='black') 
plt.plot([20,20,30],[0,10,10], color='black')
plt.plot([0,10,10],[20,20,30], color='black')
plt.plot([20,20,30],[30,20,20], color='black')

plt.plot([15,15],[0,10], '--', color='black')
plt.plot([0,10],[15,15], '--', color='black')
plt.plot([15,15],[20,30], '--', color='black')
plt.plot([20,30],[15,15], '--', color='black')

plt.savefig('fig1')

fig, ax = plt.subplots()
anim_obj, = plt.plot([],[])

# def __init__(self, speed, x, y):
#     self.speed=0.3
#     self.x=12.5
#     self.y=0

def updates(frame):
    x_array = 12.5
    y_array = [np.sin(frame*0.1)*5]
    anim_obj.set_data(x_array, y_array)
    return anim_obj

ax.set_xlim(-30,30)
ax.set_ylim(-30,30)
ani = FuncAnimation(fig, updates, frames=100)
ani.save('animation1.gif')