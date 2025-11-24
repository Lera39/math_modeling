#1
a=[12,34,2,5,67,45,16]
b=[34,6,8,12,4,56,90]
c=[5,7,98,36,59,22,41]
m=max(max(a),max(b),max(c))
s=sum(a)+sum(b)+sum(c)
print(f"максимальное число={m}, сумма={s}")

#2
name='Pisareva Lera'
a="_".join(name)
b=a.upper()
print(b)
c=[]
for q in b:
    c.append(ord(q))
# c = [ord(q) for q in b]
print(c)
d=a.lower()
print(d)
e=[]
for q1 in d:
    e.append(ord(q1))
print(e)
maxi=max(max(c), max(e))
mini=min(min(c), min(e))
print(f'наибольшее={maxi}, наименьшее={mini}')

#3
import time as tm
N=3
M=3
start=tm.time()
for i in range (M):
    for j in range (N):
        print (i,j)
        tm.sleep(1)
end=tm.time()
print(f'время выполнения функции:{end-start}')

#4
import random as r
flowers=['роза','ромашка','одуванчик']
colors=['синий','зеленый','белый','фиолетовый','черный']
b=[]
for i in range(len(flowers)):
    a=r.randint(0,len(colors)-1)
    b.append(colors[a])
flowers2=list(zip(flowers,b))
print(flowers2)

#5
name='Pisareva Valeria Aleksandrovna'
a=name.upper()
b=name.lower()
c=[]
for q in a:
    c.append(ord(q))
for q1 in b:
    c.append(ord(q1))
s=0
for i in c:
    s+=i
print(s)
