# Дополнительное задание 6 модуля. Наследование классов
import math
class Figure: #класс фигуры
    sides_count = 0

    def __init__(self, color:tuple[int, int, int], *sides, filled=False):
        self.__sides = sides  #список сторон - целые числа
        self.__color = color #список цветов в формате RGB
        self.filled = filled #закрашенный/ не закрашенный

    def get_color(self): # вызываем цвет фигуры
        return f'Цвет фигуры {self.__color}'

    def __is_valid_color(self, r,g,b): # проверяем цвет фигуры
        valid_values = 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        valid_types = isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
        return valid_types and valid_values

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    def __is_valid__sides(self, *sides):
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
            return True

    def get_sides(self):
        return sum(self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *sides):
        if len(sides) == len(self.__sides):
            valid_sides = []
            for side in sides:
                if self.__is_valid__sides(side):
                    valid_sides.append(side)

        self.__sides = valid_sides


class Circle(Figure):  #класс окружности
    sides_count = 1

    def __init__(self, color: tuple[int, int, int], length, filled=False):
        super().init(color, length, filled=filled)
        self.radius = length / (2 * math.pi)

    def get_square(self, length): # расчет по формуле площадь и длина окружности
        return len(self) ** 2 / (4 * math.pi)

class Triangle(Figure): #класс треугольники
    sides_count = 3
    def __init__(seself, color: tuple[int, int, int], height, *sides, filled=False):
        super().init(color, *sides, filled=filled)
        self.height = height

    def get_square(self): # расчет по формуле герона
        p = (len(self) / 2)
        sides = self.get_sides()
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))


class Cube(Figure): #класс кубы
    sides_count = 12
    def __init__(self, color: tuple[int, int, int], side, filled=False):
        super().init(color, *cube_sides, filled=filled)

    def get_volume(self):
        return self.get_sides()[0] ** 3


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
