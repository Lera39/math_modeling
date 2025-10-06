#Задача №1
print("Hello, World!")
print("Маша + Петя = Любовь")
print("x=3+4")
print(3+4)

#Задача №2
print(type('Hello, World!'))
print(type(3+4))
print(type(3/4))
print(type([1,2,5,10,100]))

#Задача №3
x=3
y1=((((x**3)**(1/2))/(x**3+3/x))*(4*x**7-x**5))+80*(27*x**4+12*x**3-5*x**2+10)**1/2
print(y1)
y2=(3/2+(16.7*4.32)//1)/14.5+31/12-(x**3.4)//1
print(y2)

#Задача №4
a=[1,5,'Good','Bad']
b=[9, 'Blue', 'Red', 11]
print(a[1]+b[3])
print(a[2]+b[2])
print(b[3]**a[1])
print(a+b)

#Задача №5
print("Шляпка гриба, покрытая ... кожиц..й, держится на ... ножк.. . Снизу шляпка затянута ... плёнкой. Когда её уберешь, откроется нижняя ... сторона шляпки")
print('введите 1 слово')
a=input()
print('введите 1 букву')
b=input()
print('введите 2 слово')
c=input()
print('введите 2 букву')
d=input()
print('введите 3 слово')
e=input()
print('введите 3 букву')
f=input()
print(f"Шляпка гриба, покрытая {a} кожиц{b}й, держится на {c} ножк{d} . Снизу шляпка затянута {e} плёнкой. Когда её уберешь, откроется нижняя {f} сторона шляпки")

#Задача №6
a=[]
print('введите возраст')
b=int(input())
print('введите пол')
c=input()
print('введите имя')
d=input()
print('введите город')
e=input()
print('введите класс')
f=int(input())
a.append(b)
a.append(c)
a.append(d)
a.append(e)
a.append(f)
print(a)

#Задача №1
a=int(input())
if a%2==0:
    print('четное')
else:
    print('нечетное')

#Задача №2
a=int(input())
b=int(input())
c=int(input())
for i in range(c):
    print(a)
    a=a*b