d = input()
d = int(d)
c = d % 10
b = (d // 10) %10
a = d // 1000
f = (d // 100) %10
print('Цифра в позиции тысяч равна',a)
print('Цифра в позиции сотен равна',f)
print('Цифра в позиции десятков равна',b)
print('Цифра в позиции единиц равна',c)
#n = int(input())

#*****************
print('*****************')
print('*','*', sep='               ')
print('*','*', sep='               ')
print('*****************')



a = int(input())
b = int(input())
c = a**2 + 2*a*b +b**2
d = a**2 + b**2
print('Квадрат суммы',a,'и',b,'равен',c)
print('Сумма квадратов',a,'и',b,'равен',d)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
f = a**b + c**d
print(f)

n = int(input())
k = str(n)
k1 = n+n
k2 = n+n+n
k1 = int(k1)
k2 = int(k2)
f = n + k1 + k2
print(f)