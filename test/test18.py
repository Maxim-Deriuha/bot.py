# объявление функции
def is_palindrome(text):
    k = [i for i in text if i.isalpha()]
    l= ''.join(k)
    if l[::]==l[::-1]:
        return True
    else:
        return False

# считываем данные
txt = input().lower()

# вызываем функцию
print(is_palindrome(txt))