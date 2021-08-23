def is_prime(num):
    if num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
def is_palindrome(text):
    if text[::]==text[::-1]:
        return True
    else:
        return False
def cho(num):
    if num%2==0:
        return True
    else:
        return False
    print(num%2)
# объявление функции
def is_valid_password(password):
    if len(password)>3:
        return False
    elif is_palindrome(password[0]) and is_prime(int(password[1])) and cho(int(password[2])):
        return True
    else:
        return False

# считываем данные
psw = input().split(':')
# вызываем функцию
print(is_valid_password(psw))