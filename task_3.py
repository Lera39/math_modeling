#2
from math import *
from zadanie1 import *
h=100
a=45
b=35
v=sqrt((g*h*tan(b**2))/(2*cos(a**2))*(1-tan(b)*tan(a)))
print(v)


T=200
u=300
print(e)
print((u/k*T))
N=(2/sqrt(pi))*sqrt(h*(k*T)**(3/2))*e**(u/k*T)*u**(T/2)
print(N)

#3
x0=1
y0=2
v0x=5
v0y=7
import numpy as np
from zadanie1 import g
t=np.linspace(0,5,50)
a=np.zeros((50, 3))
a[::,0]=np.linspace(0,5,50)
a[::,1]=a[::,0]*v0x+x0
a[::,2]=a[::,0]*v0y+y0-(g*a[::,0])/2
print(a)


#4
import numpy as np
trigonometry_array=np.zeros(15,20)