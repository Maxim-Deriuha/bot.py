s = input()
f = ''
if s.find('f')==s.rfind('f'):
    f = s.find('f')

else:
    f = str(s.find('f')) +' '+ str(s.rfind('f'))
if f==-1:
    print('NO')
else:
    print(f)
