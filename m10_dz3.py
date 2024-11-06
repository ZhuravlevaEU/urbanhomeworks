# Здание по теме "Блокировки и обработка ошибок"
import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):  # пополнение
        for i in range(100):
            bk = random.randint(50, 500)  # запрос средств
            self.balance += bk
            print(f'Пополнение: {bk}. Баланс: {self.balance}\n')
            if self.lock.locked() and self.balanse > 500:
                self.lock.release()  # снимаем блок

            time.sleep(0.01)

    def take(self):  # снятие
        for i in range(100):
            bk = random.randint(50, 500)  # запрос средств
            print(f'Запрос на {bk}')
            if bk <= self.balance:
                self.balance -= bk
                print(f'Снятие: {bk}. Баланс: {self.balance}\n')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()  # устанавливаем блок
            time.sleep(0.01)

if __name__ == '__main__':
    bk = Bank()
    # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
    thread1 = threading.Thread(target=Bank.deposit, args=(bk,))
    thread2 = threading.Thread(target=Bank.take, args=(bk,))

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print(f'Итоговый баланс: {bk.balance}')
