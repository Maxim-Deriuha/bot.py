import random
num = random.randrange(1,100)
def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= 100

while True:
    a = input()
    if is_valid(a)==False:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    if int(a) > num:
        print("Ваше число меньше загаданного, попробуйте еще разок")
    elif int(a) < num :
        print("Ваше число больше загаданного, попробуйте еще разок")
    else:
        print("Вы угадали, поздравляем!")
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break