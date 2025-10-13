#Работа 2
#задача 4
a=int(input())
k=0
f1=0
f2=1
while k!=a:
    print(f2)
    f3=f1+f2
    f1=f2
    f2=f3
    k+=1

#задача 5
a, b=map(int, input().split())
if b==0:
    print('нет решения')
elif a%b==0:
    print('делится')
    print(f'a/b={a/b}')
else:
    print(f'остаток: {a%b}')
    print(f'a/b={a/b}')

#задача 6
for i in range(1,10):
    for j in range(1,10):
        print(i*j, end=' ')
    print()

#дополнительный уровень
#1
a,b,c=map(int, input().split())
d=b**2-4*a*c
if d<0:
    print('нет решений')
elif d==0:
    print(f'1 решение')
    print(f'x={-b/2*a}')
else:
    print(f'2 решения')
    print(f'x1={(d**(1/2))-b /(2*a)}, x2={-(d**(1/2))+b/(2*a)}')

#2
a,b,c=map(int, input(). split())
if a+b>c and b+c>a and a+c>b:
    print('существует')
    if a==b==c:
        print('равносторонний')
    elif a==b or b==c or a==c:
        print('равнобедренный')
    else:
        print('разносторонний')
else:
    print('не сществует')

#3
a=int(input())
while a!=0:
    a1=a%10
    a//=10
    print(a1, end='')