# объявление функции
def get_month(language, number):
    lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',  'декабрь']
    lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    res=[]
    if language=='ru':
        res.append(lng_ru[number-1])
    elif language=='en':
        res.append(lng_en[number-1])
    return ''.join(res)
# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))