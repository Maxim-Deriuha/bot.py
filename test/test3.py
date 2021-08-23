a = int(input('a = '))

if a <0 or a > 36 :
    print('ошибка ввода')
elif 1<=a<=10 :
    if a % 2 ==0:
        print('черный')
    else:
        print('красный')
elif 11<=a<=18 :
    if a % 2 ==0:
        print('красный')
    else:
        print('черный')
elif 19<=a<=28 :
    if a % 2 ==0:
        print('черный')
    else:
        print('красный')
elif 29<=a<=36 :
    if a % 2 ==0:
        print('красный')
    else:
        print('черный')
else:
    print('зеленый')