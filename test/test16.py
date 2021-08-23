# объявление функции
def draw_triangle(fill, base):
    for i in range(1,base//2+1):
        print(fill*i)
    for i in range((base//2+1),0,-1):
        print(fill*i)

# основная программа
fill = input()
base = int(input())
draw_triangle(fill, base)  # вызов функции