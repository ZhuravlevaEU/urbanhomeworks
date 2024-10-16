# Создание исключений
class Car:

    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model  # название автомобиля
        self._vin = vin  # vin номер автомобиля
        self._numbers = numbers  # номера автомобиля (строка)

    def __is_valid_vin(vin_number):  # проверка на корректность vin-номер
        if not 1000000 < self._vin < 9999999:
            raise Car("Vin-номер не корректный")
        else:
            print(f"Vin номер: {vin_number})
        break

    def __is_valid_numbers(numbers):  # проверяет на корректность номер автомобиля
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Тип номера не корректный")
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            print(f"Номер: {numbers})


class ProZero(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info

    try:
        result = f( // // /)
    print(result)
    except Car():
    print("Что-то c vin пошло не так(")
    print(f"Сообщение об ошибке: {e.message}")
    print(f"Дополнительная информация: {e.extra_info}")


try:
    result = f( // // /)
    print(result)
except Car:
    print("Что-то пошло не так(")
    print(f("Сообщение об ошибке: не корректный ввод номер машины"))
