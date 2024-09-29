class House:

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, number_of_floor):
        if number_of_floor > self.number_of_floor or number_of_floor < self.number_of_floor:
            print(f'Название {self.name} этажность {number_of_floor}')
            for new_floor in range(number_of_floor):
                print(new_floor)
        else:
            print('Такого этажа нет')

    def __len__(self):
        return(f'Название {self.name} этажность {self.number_of_floor}')


    def __str__(self):
        print(f'Название {self.name} этажность {number_of_floor}')




h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

print(h1.name, h1.number_of_floor)
print(h2.name, h2.number_of_floor)


