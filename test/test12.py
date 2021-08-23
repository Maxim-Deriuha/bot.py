n = int(input())
s1=[]
s=''
s2=''
for i in range(0,n):
    s1.append(input())

k =int(input())
for i in range(0,n):
    if len(s1[i])>k-1:
        s=s1[i]
        s2+=s[k]
print(s2)