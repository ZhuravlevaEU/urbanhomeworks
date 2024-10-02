# Наследование классов
class Animal:
    def __init__(self, name, alive, fed): # живой, накормленный
        self.name = name
        self.alive = alive
        self. fed - fed

    class Mammal(Animal):
        def eat(self, food):
            if food == edible:
                print(f'{self.name} съел {food.name}')
            elif food != edible:
                print(f'{self.name} не стал есть {food.name}')

    class Predator(Animal):
        def eat(self, food):
            if food == edible:
                print(f'{self.name} съел {food.name}')
            elif food != edible:
                print(f'{self.name} не стал есть {food.name}')
class Platan:
    def __init__(self, name, edible): # съедобный
        self.name = name
        self.edible = edible

    class Flower(Platan):
        def eat(self, food):
            return self.eat(food)

    class Fruit (Platan):
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
