# задание по теме "Потоки на классах"
# Импортируем необходимые модули и функции
import threading
import time


class Knight(threading.Thread): # создаем свой класс
def __init__(self, str, int, counter, delay):
    threading.Thread.__init__(self)
    self.str = str
    self.int = 100
    self.counter = 0
    self.delay = delay

def run (self):
    print(f'{self.str}, на нас напали!')
    time.sleep(1) # прошел один день
    while self.int < 100:
        print(f'{self.str} сражается {self.counter} кол-во дней, осталось {self.int} воинов')
        self.counter +=1
        self.int -=1

    print(f'        {self.str} одержал победу за {self.counter} день(дней).')


# Создаем 2a потока с аргументами из задачи
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запускаем 4е потока с аргументами из задачи
first_knight.start()
second_knight.start()

# Остановим текущий поток
first_knight.join()
second_knight.join()
