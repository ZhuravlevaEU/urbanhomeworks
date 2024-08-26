# Задача "Распаковка"
# 1 Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Проверка вызовов функции с разным количеством аргументов
print_params(a=1, b='строка', c=True)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
# Все работает!!!

# 2 Распаковка параметров
values_list = [1, 'два', True]
values_dict = {'a':1, 'b': 'строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)

# 3 Распаковка + отдельные параметры
values_list_2 = [1, True]
print_params(*values_list_2, 42)
# Работает!!!
