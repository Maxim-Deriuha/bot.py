a = int(input())
ost=a%10
counter_ost=0
counter_3=0
counter_2=0
sum_5=0
pro_7=1
counter_0_5=0

while a!=0:
    if a %10==3:
        counter_3+=1
    if a%10 ==ost:
        counter_ost+=1
    if (a%10)%2==0:
        counter_2+=1
    if a%10>5:
        sum_5+=a%10
    if a%10>7:
        pro_7*=a%10
    if a%10==0 or a%10 ==5:
        counter_0_5+=1
    a//=10

print(counter_3)
print(counter_ost)
print(counter_2)
print(sum_5)
print(pro_7)
print(counter_0_5)







