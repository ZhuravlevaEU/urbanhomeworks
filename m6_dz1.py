# Наследование классов
class Platan:
    edible = False
    def __init__(self, name):  # съедобный
        self.name = name

class Animal:
    alive = True # живой, сытый
    fed = False
    def __init__(self, name):
        self.name = name
        
    def eat(self, food):  # еда
        input('Введите растение', self.food)
        if self.food == edible:
            print(f'{self.name} съел {self.food}')
            self.fed = True
        elif self.food != edible:
            print(f'{self.name} не стал есть {self.food}')
            self.alive = False

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Platan):
    pass

class Fruit(Platan):
    edible = True
    pass



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
