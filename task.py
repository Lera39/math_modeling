#1
import matplotlib.pyplot as plt
plt.plot([1,1,5,5,1],[1,5,5,1,1])
plt.axis('equal')
plt.savefig('task1.png')

#2
import matplotlib.pyplot as plt
import numpy as np

q=int(input())
def giperbola(N):
    x=np.arange(10,10,0.1)
    y=1/x
    plt.plot(x,y)
    plt.savefig('task2.png')

giperbola(q)

#3
import matplotlib.pyplot as plt
import numpy as np
a=7
b=21
x=np.arange(-10,10,0.1)
y=np.arange(-10,10,0.1)
X,Y=np.meshgrid(x,y)
fxy=X**2/a+Y**2/b-1
plt.contour(X, Y, fxy, levels=[0])
plt.axis('equal')
plt.savefig('task3.png')

#4
import matplotlib.pyplot as plt
import numpy as np
pi=3.1415
e=2.71

k=20

phi=np.arange(0*pi,8*pi,0.01)
r=k*e*phi
y=r*np.sin(phi)
x=r*np.cos(phi)
plt.plot(x,y)
plt.axis('equal')
plt.savefig('task4_1.png')

#жезл
phi=np.arange(0*pi,8*pi,0.01)
r=k/(phi**1/2)
y=r*np.sin(phi)
x=r*np.cos(phi)
plt.plot(x,y)
plt.axis('equal')
plt.savefig('task4_2.png')

#роза
phi=np.arange(0.01*pi,8*pi,0.01)
r=np.sin(k*phi)
y=r*np.sin(phi)
x=r*np.cos(phi)
plt.plot(x,y)
plt.axis('equal')
plt.savefig('task4_3.png')
