
name = str(input())
name2 = str(input())
name3 = str(input())
kol = len(name)
kol2 = len(name2)
kol3 = len(name3)
d = (2*kol2-kol3-kol)*(2*kol3-kol2-kol)*(2*kol-kol2-kol3)
if d==0:
    print('YES')
else:
    print('NO')