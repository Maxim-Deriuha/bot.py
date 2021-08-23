num  = int(input())
s=[]
k=0
for i in range(0,num):
    s.append(int(input()))
for i in range(0,num):
    if i%2!=0:
        del s[i-k]
        k+=1
print(s)