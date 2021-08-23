n = input()
n = int(n[1:])
a =''
s=[]
for i in range(n):
    a = input()
    r = a.find('#')
    if '#' in a:
        a=a[0:r]
    s.append(a.rstrip())
print(*s,sep='\n')