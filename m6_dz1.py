# Наследование классов
class Animal:
    def __init__(self, name, alive, fed):  # живой, сытый
        self.name = name
        self.alive = True
        self.fed = False
        self.edible = False


def eat(self, food, edible):  # еда
    input('Введите растение', food.name)
    if food.name == self.edible:
        print(f'{self.name} съел {food.name}')
        self.fed = True
    elif self.food != edible:
        print(f'{self.name} не стал есть {food.name}')
        self.alive = False


class Mammal(Animal):
    input('Введите животное', self.name)


class Predator(Animal):
    super().__init__(self, food)


class Platan:
    def __init__(self, name, edible):  # съедобный
        self.name = name
        self.edible = False


class Flower(Platan):
    def eat(self, food):
        return self.eat(food)


class Fruit(Platan):
    super().__init__(self, edible)

    def eat(self, food):
        return self.eat(food)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
