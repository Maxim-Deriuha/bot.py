s = input()
a = 0
for i in range(0,len(s)):
    if i %3==0:
        print(i)
        s = s[:i-a] + '' + s[i+1-a:]
        a+=1
print(s)