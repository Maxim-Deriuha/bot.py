from math import *
a = float(input())
b = float(input())
c = float(input())
d = (b**2) - (4*a*c)
if a == 0 or d <0 :
    print('Нет корней')
elif d >0 :
    x1 = (-b+sqrt(d))/(2*a)
    x2 =  (-b-sqrt(d))/(2*a)
    print(min(x1 ,x2))
    print(max(x1,x2))
else:
    x = (-b) / (2*a)
    print(x)
