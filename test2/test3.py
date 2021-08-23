kov = int(input())
res = ''
st = []
for i in range(kov):
    st.append(int(input()))
num = int(input())
if len(st) == 1:
    res = 'НЕТ'
else:
    for i in range(len(st)):
        for k in range(i+1, len(st)):
            if st[i] * st[k] == num:
                res = 'ДА'
                break
            else:
                res = 'НЕТ'
        if res == 'ДА':
            break
print(res)
