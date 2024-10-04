# Доступ к родителю. Переопределение свойств
class Vehicle: # Транспорт
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # список цветов


def __init__(self, owner, __model, __engine_power, __color):
    self.owner = input('Владелец: '), owner  # в ладелец
    self.__model = input('Модель машины: '), __model
    self.__engine_power = input('Мощность двигателя: '), __engine_power  # можность двигателя
    self.__color = input('Цвет машины: '), __color  # название цвета


def set_color(self, __color):
    new_color = input('Какого цвета машину вы хотите?')
    if new_color in range(1, self.__COLOR_VARIANTS):
        self.__color = new_color
    else:
        print(f'Нельзя сменить цвет на ', {new_color})

def get_model(self, __model):
        print(f'Модель: ', {self.__model})

def get_horsepower(self, __engine_power):
        print(f'Мощность двигателя: ', {self.__engine_power})

def get_color(self, __color):
        print(f'Цвет: ', {self.__color})

def print_info(self):
        print(get_model, get_horsepower, get_color)

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
