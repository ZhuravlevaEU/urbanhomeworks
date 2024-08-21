# создаю кортеж
tuple_ = (1, 2, 3, 4, 5, False, 'комар')
immutable_var = tuple_
print(immutable_var)
# заменю элемент кортежа
# tuple_[0] = 9 TypeError: 'tuple' object does not support item assignment
# кортеж представляет собой единый объект, не подлежащий поелементому преобразованию
print(immutable_var)
# заменяю первый элемент списка
a, b, c, d, e, f, g = tuple_
a = 7
tuple_ = (7, 3, 4, 5, False, 'комар')
print(tuple_)
# создаю новую переменную, содержащую список
mutabele_list = [4, 5, False, 'комар']
# изменяю элементы списка
mutabele_list.append(True)
print(mutabele_list)
