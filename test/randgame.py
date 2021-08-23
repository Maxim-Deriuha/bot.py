import random

num  = random.randint(0, 101)
k= 0
while True:

    chi = input("Введите число :")
    if not chi or chi == "exit" :
        break
    if not chi.isdigit():
        print("Введите правильное число !")
        continue
    chi1 = int(chi)
    if chi1 > num:
        print("Загадонное число меньше")
    elif chi1 < num :
        print("Загадонное число больше")
    else:
        print("Совершенно верно!")
        break
