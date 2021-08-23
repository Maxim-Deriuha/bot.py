b = 1
fib = 1
sum = 0
te = ''
v = '1 1 '
n = int(input())
for _ in range(2,n):
   if n<2:
       print(1)
   else:
        sum = b + fib
        b = fib
        fib = sum
        te = str(fib)
        v = v + te + ' '

print(v)