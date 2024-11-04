# Задача "Потоковая запись в файлы"
# Импортируем необходимые модули и функции
import threading
import time
from time import sleep

# Объявляем функцию
def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf-8')
    word_count = int(word_count)
    file_name = str(file_name)
    for number in range(word_count + 1):
        time.sleep(0.1)
        file.write(f'Какое-то слово № {number} \n')

    print(f'Завершилась запись в файл {file_name}')

# Засекаем время начала работы
start_time_fun = time.time()
# Запускаем 4е раза функцию с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
# Засекаем время окончания работы
end_time_fun = time.time()
# Выводим разницу начала и конца работы функций
diff_time = end_time_fun - start_time_fun
print('Работа функций: ', round(diff_time, 5))
# Засекаем время начала работы
start_time = time.time()
# Создаем 4е потока с аргументами из задачи
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
# Запускаем 4е потока с аргументами из задачи
thread1.start()
thread2.start()
thread3.start()
thread4.start()
# Делаем остановку основного потока
thread1.join()
# Выводим разницу начала и конца работы потоков
end_time = time.time()
diff_time = end_time - start_time
print('Работа потоков: ', round(diff_time, 5))
