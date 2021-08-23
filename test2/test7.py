n = int(input())
for k in range(1, n + 1):
    print(k)
    my_list = [[0] * k] * n
print(*my_list)
for i in range(n):
    my_list[0][i] = i + 1
print(*my_list, sep='\n')
