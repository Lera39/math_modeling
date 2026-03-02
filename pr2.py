import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
anim_obj, = plt.plot([],[])

def plane():
    x_array = 
    y_array = np.arange(14.9,15.1,0.001)
    anim_obj.set_data(x_array, y_array)
    return anim_obj

A_array = np.arange(-4,4,0.1)
ani = FuncAnimation(fig, plane, frames=A_array)
ax.set_xlim(-4*np.pi,4*np.pi)
ax.set_ylim(-4*np.pi,4*np.pi)
ani.save('animation1.gif')
