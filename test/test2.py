x = str(input())
y = str(input())

if (x =='красный' and y =='синий') or (y =='красный' and x =='синий'):
    print('фиолетовый')
elif (x =='красный' and y =='желтый') or (y =='красный' and x =='желтый'):
    print('оранжевый')
elif (x =='синий' and y =='желтый') or (y =='синий' and x =='желтый'):
    print('зеленый')
elif x==y and (x =='синий' or x =='желтый' or x =='красный'):
    print(y)
else:
    print('ошибка цвета')



