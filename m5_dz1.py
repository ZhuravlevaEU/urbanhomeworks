class House:


    def __init__(self, name, number_of_floor, go_tu):
        self.name = name
        self.number_of_floor = number_of_floor
        self.go_tu = go_tu

    def go_tu(self, number_of_floor):
        if new_floor > self.number_of_floor or new_floor < self.number_of_floor:
            print(f'Название {self.name} этажность {number_of_floor}')
        else:
            print('Такого этажа нет')
            for new_floor = range(number_of_floor):


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

print(h1.name, h1.number_of_floor)
print(h2.name, h2.number_of_floor)
