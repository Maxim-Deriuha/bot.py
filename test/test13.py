
n = int(input())
s=[]
s2=[]
for i in range(n):
    s.append(input())
k=int(input())
for i in range(k):
    s2.append(input())
for r in range(len(s)):
    print(s[r])
    for g in range(len(s2)):
        if s2[g].lower() not in s[r].lower():
            break
        else:
            print(s[r])
