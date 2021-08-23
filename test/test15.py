l = [i for  i in input().split('-')]
if  ''.join(l).isdigit():
    if l[0]=='7':
        del l[0]
    if len(l[0])==3 and len(l[1])==3 and len((l[2]))==4:
         print('YES')
    else:
        print('NO')
else:
    print('NO')