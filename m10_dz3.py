# Здание по теме "Блокировки и обработка ошибок"
import threading
import random
import time

class Bank:
    counter = 0 # число транзакций пополнения и снятия
    lock = threading.Lock()
    def __init__(self, balance):
        self.balance = bk

    def deposit(self): # пополнение
        global counter
        while counter < 100:
            bk = random.randint(50, 500) # запрос средств
            lock.release() # снимаем блок
            try:
                self.balance += bk
                print(f'Пополнение: {bk}. Баланс: {self.balance}\n')
            except Exception:
                pass
            finally:
                time.sleep(0.01)
                counter += 1

    def take(self): # снятие
        global counter
        lock.acquire()  # устанавливаем блок
        while counter < 100:
            bk = random.randint(50, 500) # запрос средств
            print(f'Запрос на {bk}')
            try:
                if bk <= self.balance:
                    self.balance -= bk
                    print(f'Снятие: {bk}. Баланс: {self.balance}\n')
                else:
                    print('Запрос отклонён, недостаточно средств')
            finally:
                time.sleep(0.01)
                counter += 1


bk = Bank()
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
thread1 = threading.Thread(target=Bank.deposit, args=(bk,))
thread2 = threading.Thread(target=Bank.take, args=(bk,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(f'Итоговый баланс: {bk.balance}')

