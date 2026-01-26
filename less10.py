import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# #1
# plt.plot([1,2,3,4,5],[11,9,5,6,8])
# plt.savefig('fig1.png')

# #2
# plt.plot([1,2,3,4,5],[1,4,9,16,25])
# plt.savefig('fig2.png')

#задачи на функции

# #1
# x=np.arange(-2,2,0.01)
# y=x**3
# plt.axis('equal')
# plt.plot(x,y)
# plt.savefig('fig3.png')

# #4
# x=np.arange(-5,5,0.01)
# y=np.sin(x)
# plt.axis('equal')
# plt.plot(x,y)
# plt.savefig('fig4.png')

# #5
# x=np.arange(-5,5,0.01)
# y=x**(1/2)
# plt.axis('equal')
# plt.plot(x,y)
# plt.savefig('fig5.png')

#параметр

# #1
# t=np.arange(0,2*np.pi,0.01)
# x=np.sin(t)
# y=2*np.cos(t)
# plt.axis('equal')
# plt.plot(x,y)
# plt.savefig('fig6.png')

# #2
# t=np.arange(-1,1,0.01)
# x=t
# y=t
# plt.axis('equal')
# plt.plot(x,y)
# plt.savefig('fig7.png')

#гифка

# #1
# fig, ax = plt.subplots()
# anim_obj, = plt.plot([],[])
# def update (z_frame):
#     A=z_frame
#     x_array = np.arange(-4*np.pi, 4*np.pi,0.01)
#     y_array = A*np.sin(x_array)
#     anim_obj.set_data(x_array, y_array)
#     return anim_obj
# A_array = np.arange(-4,4,0.1)
# ani = FuncAnimation(fig, update, frames=A_array)
# ax.set_xlim(-4*np.pi,4*np.pi)
# ax.set_ylim(-4*np.pi,4*np.pi)
# ani.save('animation1.gif')

#2
fig, ax = plt.subplots()
anim_obj, = plt.plot([],[])

def update (z_frame):
    A=z_frame
    t=np.arange(0,2*np.pi,0.01)
    x=np.sin(t)*A+A
    y=np.cos(t)+A
    anim_obj.set_data(x, y)
    return anim_obj

A_array=np.arange(1, 5, 0.05)
ani = FuncAnimation(fig, update, frames=A_array)
ax.set_xlim(-4,4)
ax.set_ylim(-4,4)
ani.save('animation2.gif')