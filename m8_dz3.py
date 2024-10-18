# Создание исключений
class IncorrectCarNumbers(Exception):
    def __init__(self, message, *args):
        self.message = message

class IncorrectVinNumbers(Exception):
    def __init__(self, message, *args):
        self.message = message

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model # название автомобиля
        if self.__is_valid_vin(vin):
            self.__vin = vin  # vin-номер автомобиля
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers  # номера автомобиля (строка)

    def __is_valid_vin(vin_numbers):  # проверка на корректность vin-номер
        if not isinstance(vin_numbers, int):
            raise IncorrectVinNumbers("Vin-номер не корректный")
        elif vin_numbers not in range(1000000, 9999999):
            raise IncorrectVinNumbers('Неверный диапазон для vin номера',
            f'Диапазон: 1000000-9999999 Ваш Vin номер: {vin_numbers}')
        return True

    def __is_valid_numbers(numbers):  # проверяет на корректность номер автомобиля
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Тип номера не корректный")
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера',
                                      f'Ваш номер {numbers} содержит не правильное количество цифр')
        return True


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumbers as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
