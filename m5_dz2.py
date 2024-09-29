class House:

    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, number_of_floors):
        if number_of_floors > self.number_of_floors or number_of_floors < self.number_of_floors:
            print(f'Название {self.name} этажность {number_of_floors}')
            for new_floors in range(number_of_floors):
                print(new_floors)
        else:
            print('Такого этажа нет')

    def __str__(self):
        return f'Название {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(len(h1))
print(len(h2))
