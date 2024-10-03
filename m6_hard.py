# Дополнительное задание 6 модуля. Наследование классов

class Figure: #класс фигуры
    sides_count = 0

    def __init__(self, __sides, __color, filled):
        self.__sides = sides  #список сторон - целые числа
        self.__color = colors #список цветов в формате RGB
        self.filled = filleds #закрашенный/ не закрашенный

    def set_color(self):
        for r in range(1, 255):
            for g in range(1, 255):
                for b in range(1, 255):
                    self.__color(r, g, b) = [rgb]
        brek
            print(f' Цвет - прежний')

    def __is_valid_color(self, r,g,b):
        #проверка цвета
        if self.__color > 0 and self.__color == int
            print(f'True')
        else:
            print(f'False')
    def get_color(self):
        return f'Цвет фигуры {self.__color}'

    def set_sides(self, *new_sides):
        self.__sides() = сумма всех сторон
        sides_count
        """for arg in args:
            if isinstance(arg, str):
                total_sum += len(arg)
            elif isinstance(arg, (int, float)):
                total_sum += arg
            elif isinstance(arg, (list, tuple, set)):
                total_sum += all_sum(*arg)
            elif isinstance(arg, dict):
                total_sum += all_sum(*arg.items())
            elif arg is None:
                pass
        return total_sum"""

    def __is_valid__sides(self, bool):

    def get_sides(self):
        return f'Список сторон {self.__sides}'

    def __len__(self, perimetr):
        ????

class Circle(Figure):  #класс окружности
    sides_count = 1
    def __init__(self, __radius):
        self.__radius = __radius

    def get_square(self, length): # расчет по формуле площадь и длина окружности

class Triangle(Figure): #класс треугольники
    sides_count = 3
    def __init__(self, __a, __b, __c):
        self.__a = first
        self.__b = second
        self.__c = third

    def get_square(self): # расчет по формуле герона


class Cube(Figure): #класс кубы
    sides_count = 12
    def __init__(self, __sades):
        self.__sades = sides
    def get_volume(self, sades): # объем куба
        self.__sades =


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
