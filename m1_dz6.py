# создаю словарь
my_dict = {'Denis': 1999, 'Anton': 2000, 'Alex': 2001}
print(my_dict)
# выбираю первое значение по ключу
print(my_dict['Denis'])
# добавление 2х пар элементов
my_dict.update({'Pol': 2000, 'Kat': 2002})
print(my_dict)
# удаление 1й пары по ключу
print(my_dict.pop('Denis'))
# создаю множество
my_set = {1, 2, 3, 1, 2, 3, True, False, 'Привет!'}
print(my_set)
# добавление 2х элементов
my_set.update([5, 7])
print(my_set)
# Ура!