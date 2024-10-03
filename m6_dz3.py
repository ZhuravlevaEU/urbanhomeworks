# Множественное наследование
class Horse: # класс лошадь
    def __init__(self, x_distance, sound):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.dx = dx #путь

class Eagl: # класс орел
    def __init__(self, y_distance, sound):
        self.x_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
        
    def fly(self, dy):
        self.dy = dy #ауть

class Pegasus(Horse): # класс Пегас
    def __init__(self, x_distance, sound):
        super().__init__(x_distance, sound)

    def move(self, dx, dy):
        super().run(self, dx)
        super().fly(self, dy)

    def get_pos(self):
        print(f'Положение Пегаса: {self.x_distance}, {self.y_distsnce}')

    def voice(self, sond):
        super().__init__(self, sound)
        print(f'Пегас говорит: {self.sound}')


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

