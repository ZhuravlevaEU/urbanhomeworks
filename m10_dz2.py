# задание по теме "Потоки на классах"
# Импортируем необходимые модули и функции
import threading
import time


class Knight(threading.Thread): # создаем свой класс
    def __init__(self, str, int):
        threading.Thread.__init__(self)
        self.str = str # имя рыцаря
        self.int = 100 # сила его

    def run (self):
        print(f'{self.str}, на нас напали!')
        time.sleep(1) # прошел один день
        enemies_counter = 100 # количество воинов
        day = 0 # количество дней сражения
        while self.int > 0:
            enemies_counter -= self.int
            day += 1
            if enemies_counter < self.int:
                enemies_counter = 0
            print(f'{self.str} сражается {day} кол-во дней, осталось {enemies_counter} воинов')
            sleep(1)

        print(f'{self.str} одержал победу за {self.counter} день(дней).')


# Создаем 2a потока с аргументами из задачи
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запускаем 4е потока с аргументами из задачи
first_knight.start()
second_knight.start()

# Остановим текущий поток
first_knight.join()
second_knight.join()
