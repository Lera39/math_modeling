#1
import numpy as np
def my_sum(a):
    b=0
    for i in range (len(a)):
        b+=a[i]
    return b/len(a)
a=np.array([12,45,15,25,13,46,57,46,3,56,4,7,11,23])
print(my_sum(a))

#2
import numpy as np
def funk(a):
    b=1
    for i in range(len(a)):
        b*=a[i]
    return b
a=np.array([12,45,15,25,13,11,23])
print(funk(a))

#3
from const import g
def energy(m,v,h):
    en=((m*v**2)/2)+(m*g*h)
    return en
m2=15
h2=10
v2=7
print(energy(m2,v2,h2))

#4
import numpy as np
def f(a,b,N):
    return np.linspace(a,b,N)**2
print(f(0,10,11))

#5
from const import pi
def S(a,b,c,h,r):
    if a=="прямоугольник":
        pl=b*c
    elif a=="треугольник":
        pl=b*h/2
    elif a=="круг":
        pl=pi*r**2
    return pl
print(S('круг',12,13,14,15))


#1
def f(a,n):
    a1=a
    if n>0:
        for i in range(n-1):
            a*=a1
    elif n==0:
        a=1
    elif n<0:
        for i in range (-n+1):
            a*=1/a1
    return a
print(f(5,-2))

#2
def fib(n):
    f1=0
    f2=1
    for i in range(n-2):
        f3=f1+f2
        f1=f2
        f2=f3
    return f2
print(fib(7))