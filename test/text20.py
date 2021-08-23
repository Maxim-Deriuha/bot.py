# объявление функции
def convert_to_python_case(text):
    k = [i.lower() for i in text]
    l = [ i for i in text]
    h=[]
    h.append(k[0])
    for i in range(1,len(k)):
        if k[i]==l[i]:
            h.append(k[i])
        else:
            h.append('_'+k[i])
    return ''.join(h)


# считываем данные
txt = input()
# вызываем функцию
print(convert_to_python_case(txt))