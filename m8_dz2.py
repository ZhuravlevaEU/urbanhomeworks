# ТЕМА: Сложные моменты и исключения в стеке вызовов функции
# Задача "План перехват":
# Функция personal_sum(numbers):
# Должна принимать коллекцию numbers.
# Подсчитывать сумму чисел в numbers путём перебора и увеличивать переменную result.
# Если же при переборе встречается данное типа отличного от числового,
# то обработать исключение TypeError, увеличив счётчик incorrect_data на 1.
# В конечном итоге функция возвращает кортеж из двух значений: result - сумма чисел,
# incorrect_data - кол-во некорректных данных.

def personal_sum(*numbers): # Подсчитываем сумму чисел путём перебора и увеличиваем переменную result
    result = 0
    incorrect_data = 0
    for i in numbers:
        for j in i:
            try: # Если при переборе встречаем данное другого типа - отличного от числового
                result += j
            except TypeError: # то обработаем исключение TypeError, увеличивая счётчик incorrect_data на 1
                incorrect_data += 1
                print(f'некорректный тип данных для подсчета суммы - {j}')
    return result, incorrect_data # функция возвращает кортеж из двух значений: result - сумма чисел,
    # incorrect_data - кол-во некорректных данных

# Функция calculate_average(numbers)

def calculate_average(*numbers):
    if isinstance(*numbers, int): # проверяем тип данных, чтобы были числа
        return None
    try:
        tuple_pers_sum = personal_sum(*numbers) # считаем сумму всех элементов коллекции
        # Среднее арифметическое
        return tuple_pers_sum[0] / (len(*numbers) - tuple_pers_sum[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        return f'В numbers записан некорректный тип данных'

# Вывод результата
calculate_average("1, 2, 3")
calculate_average([1, "Строка", 3, "Ещё Строка"])
calculate_average(567)
calculate_average([42, 15, 36, 13])

