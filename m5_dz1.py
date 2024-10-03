class House:

    def __init__(self, name, floors):
        self.name = name
        self.number_of_floor = floors


    def go_to(self, number_of_floor):
        if number_of_floor > self.number_of_floor or number_of_floor < self.number_of_floor:
            print(f'Название {self.name} этажность {number_of_floor}')
            for new_floor in range(1, number_of_floor+1):
                print(new_floor)
        else:
            print('Такого этажа нет')



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

print(h1.name, h1.number_of_floor)
print(h2.name, h2.number_of_floor)
