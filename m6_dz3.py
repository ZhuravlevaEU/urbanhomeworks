# Множественное наследование
class Horse:

    def __init__(self):
        self.x_distance = 0 # пройденный путь
        self.sound = 'Frrr' # звук, который издаёт лошадь

    def run(self, dx):
        self.x_distance = self.dx + dx

class Eagl:  # класс орел
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance = self.dy + dy

class Pegasus(Horse, Eagl):  # класс Пегас
    def __init__(self):
        Horse.__init__(self)
        Eagl.__init__(self)

    def move(self, dx, dy):
        super().run(self.y_distance, dx)
        super().fly(self.y_distance, dy)

    def get_pos(self):
        return f'Положение Пегаса: {self.x_distance}, {self.y_distance}'

    def voice(self):
        print(f'Пегас говорит: {self.sound}')


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

