
import matplotlib.pyplot as plt
plt.plot([1,2,3],[5,7,10])
plt.savefig('less7.png')

import numpy as numpy
def parabola_plotter(a=1, b=1, c=0):
    x=np.arange(-10,10,0.01)
    y=a*x**2+b*x+c
    plt.plot(x, y, label='my parabola')
    plt.savefig('fig_pr.png')


import matplotlib.pyplot as plt
import numpy as np
radius=10
x=np.arange(-2*radius, 2*radius, 0.1)
y=np.arange(-2*radius, 2*radius, 0.1)
X,Y=np.meshgrid(x,y)
fxy=X**2+Y**2-radius**2
plt.contour(X, Y, fxy, levels=[0])
plt.axis('equal')
plt.savefig('circle.png')