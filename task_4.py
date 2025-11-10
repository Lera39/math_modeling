#1
import numpy as np
a=[[4,8,12],[7,89,34],[23,56,17]]
b=[[12,46,2],[84,34,1],[8,6,13]]
c=[]
for i in range(3):
    for j in range(3):
        c.append(max((a[i][j]),(b[i][j])))
print(c)


#2
import numpy as np
a=[1,2,3,4,5,6,7,8]
print(a)
b=int(input())
c=int(input())
d=(a[:c-1])
e=(a[c-1:])
f=[*d,b,*e]
print(f)

#3
import numpy as np
a=np.array([[3,4,45],[46,12,8],[10,22,25],[15,30,55]])
for i in range(3):
    print(max(a[:,i]))
