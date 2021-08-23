count = int(input())
I = 0
II = 0
III = 0
IV = 0
for i in range(count):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        I += 1
    elif x < 0 and y > 0:
        II += 1
    elif x < 0 and y < 0:
        III += 1
    elif x > 0 and y < 0:
        IV += 1
print('Первая четверть: ', I)
print('Вторая четверть: ', II)
print('Третья четверть: ', III)
print('Четвертая четверть: ', IV)
