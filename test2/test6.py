for i in range(int(input())):
    s, v, x = input(), 'anton', 0
    for sym in s:
        if sym == v[x]:
            x += 1
        if x == 5:
            print(i + 1, end=' ')
            break
